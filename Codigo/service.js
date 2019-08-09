const OracleBot = require('@oracle/bots-node-sdk');
const { WebhookClient, WebhookEvent } = OracleBot.Middleware;
const path = require('path')
const { spawn } = require('child_process')

module.exports = (app) => {
  const logger = console;
  // initialize the application with OracleBot
  OracleBot.init(app, {
    logger,
  });

  // add webhook integration
  const webhook = new WebhookClient({
    channel: {
      url: 'https://botv2phx1I0044H0105B5bots-mpaasocimt.botmxp.ocp.oraclecloud.com:443/connectors/v1/tenants/idcs-100b89d671b54afca3069fe360e4bad4/listeners/webhook/channels/deff9d29-26cd-428e-b110-9fd0869dca71',
      secret: 'R2o9cWV7oAyvCrLDbLLatkTsqr05z3BG',
    }
  });
  // Add webhook event handlers (optional)
  webhook
    .on(WebhookEvent.ERROR, err => logger.error('Error:', err.message))
    .on(WebhookEvent.MESSAGE_SENT, message => logger.info('Message to bot:', message))
    .on(WebhookEvent.MESSAGE_RECEIVED, message => {
      // message was received from bot. forward to messaging client.
      logger.info('Message from bot:', message);
      console.log(MESSAGE_RECEIVED);
      // TODO: implement send to client...
      logger.info('MessageReceived: ',MESSAGE_RECEIVED);
    });

  // Create endpoint for bot webhook channel configurtion (Outgoing URI)
  // NOTE: webhook.receiver also supports using a callback as a replacement for WebhookEvent.MESSAGE_RECEIVED.
  //  - Useful in cases where custom validations, etc need to be performed.


  // Integrate with messaging client according to their specific SDKs, etc.
  app.post('/test/message', (req, res) => {
    const { user, text } = req.body;
    // construct message to bot from the client message format
    const MessageModel = webhook.MessageModel();
    const message = {
      userId: user,
      messagePayload: MessageModel.textConversationMessage(text)
    };

    // send to bot webhook channel
    webhook.send(message)
      .then(() => res.send('ok'), e => res.status(400).end(e.message));

  });

    app.post('/', (req, res) => {
    const response = webhook.receiver();
    res.set('Content-Type', 'application/json');

    res.send(response);
    var resjson = res.req.body;
    console.log(resjson.messagePayload.text);
    console.log("Start TTS");
    var spawn = require("child_process").spawn;
    // var process = spawn('python3', ['/home/opc/Python/tty.py', resjson.messagePayload.text]);
    var process = spawn('python3', ['/home/opc/Python/tts.py', resjson.messagePayload.text]);
    process.stdout.on('data', function(data) { 
        console.log(data.toString()); 
    } ) 
    console.log("End TTS");
  });
}
