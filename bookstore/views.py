import logging
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import git
import hmac
import hashlib

logger = logging.getLogger(__name__)

@csrf_exempt
def update(request):
    secret = 'seu_token_secreto'  # Token configurado no webhook do GitHub
    if request.method == "POST":
        # Verificação de assinatura (se você configurou um secret no GitHub)
        signature = request.headers.get('X-Hub-Signature')
        if signature:
            mac = hmac.new(secret.encode(), msg=request.body, digestmod=hashlib.sha1)
            calculated_signature = 'sha1=' + mac.hexdigest()
            if not hmac.compare_digest(calculated_signature, signature):
                return HttpResponseForbidden("Invalid signature")

        try:
            repo = git.Repo('/home/monosodrac/bookstore')
            origin = repo.remotes.origin
            logger.info("Pulling latest code from repository...")
            origin.pull()  # Faz o pull do repositório
            logger.info("Code updated successfully.")
            return HttpResponse("Updated code on PythonAnywhere")
        except git.exc.GitCommandError as e:
            logger.error(f"Git pull failed: {e}")
            return HttpResponse(f"Git pull failed: {e}")
        except Exception as e:
            logger.error(f"Error: {e}")
            return HttpResponse(f"Error: {e}")
    else:
        return HttpResponse("Invalid method. Only POST is allowed.")
