class GetAnswerOneHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
    # type: (HandlerInput) -> bool
    
        
    return (
        ask_utils.is_request_type("IntentRequest")(handler_input)
            and ask_utils.is_intent_name("GetAnswerOne")(handler_input)
    )
    
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #speak_output =  f"Welcome to the Yes handler."
        
        #speak_output = ''
        
        # get the current session attributes, creating an object you can read/update
        session_attributes = handler_input.attributes_manager.session_attributes
        
        if (('current_ancestor' in session_attributes.keys() and
        session_attributes["current_ancestor"] == None) or
            'current_ancestor' not in session_attributes.keys()):

            speak_output = "lo siento he perdido la conexión a tu ancestro"

            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
            )
        
        cAnswer = session_attributes["current_ancestor"]["respuesta1"]
        #year = ask_utils.request_util.get_slot(handler_input, "year").value
        #month = ask_utils.request_util.get_slot(handler_input, "month").value

        # Share the answer
        speak_output = f'{cAnswer}'
        
        
        #====================================================================
        # Add a visual with Alexa Layouts
        #====================================================================
        # Import an Alexa Presentation Language (APL) template
        with open("./documents/APL_simple.json") as apl_doc:
            apl_simple = json.load(apl_doc)

        if ask_utils.get_supported_interfaces(
            handler_input).alexa_presentation_apl is not None:
            handler_input.response_builder.add_directive(
            RenderDocumentDirective(
                document=apl_simple,
                datasources={
                    "myData": {
                        #====================================================================
                        # Set a headline and subhead to display on the screen if there is one
                        #====================================================================
                        "Title": f'',
                        "Subtitle": f'{cAnswer}',
                        #"Title": 'Y dijiste "SI"!!', 
                        #"Subtitle": 'Juguemos secretos familiares',  #"Subtitle": 'Play secretos familiares.',
                    }
                }
            )
        )
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )