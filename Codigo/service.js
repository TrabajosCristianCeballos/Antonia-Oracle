const OracleBot = require('@oracle/bots-node-sdk');
const { WebhookClient, WebhookEvent } = OracleBot.Middleware;

module.exports = (app) => {
  const logger = console;
  // initialize the application with OracleBot
  OracleBot.init(app, {
    logger,
  });

  // add webhook integration
  const webhook = new WebhookClient({
    channel: {
      url: 'https://botv2phx1I0044H0105B5bots-mpaasocimt.botmxp.ocp.oraclecloud.com:443/connectors/v1/tenants/idcs-100b89d671b54afca3069fe360e4bad4/listeners/webhook/channels/25eb87fc-7945-4d29-9755-0817b16b29ea',
      secret: 'k1P4Vgj1kdDHataDZpSWA0vwDbElWhXS',
    }
  });
  // Add webhook event handlers (optional)
  webhook
    .on(WebhookEvent.ERROR, err => logger.error('Error:', err.message))
    .on(WebhookEvent.MESSAGE_SENT, message => logger.info('Message to bot:', message))
    .on(WebhookEvent.MESSAGE_RECEIVED, message => {
      // message was received from bot. forward to messaging client.
      logger.info('Message from bot:', message);
//console.log(MESSAGE_RECEIVED);
      // TODO: implement send to client...
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

fs.readFile('respuesta.json', 'utf8', function readFileCallback(err, data){ 
    if (err){ 
     console.log(err); 
    } else { 
    obj = JSON.parse(data); //now it an object 
    obj.table.push({user: 2, text:3}); //add some data 
    json = JSON.stringify(obj); //convert it back to json 
    fs.writeFile('respuesta.json', json, 'utf8', callback); // write it back 
}}); 
  });
}
