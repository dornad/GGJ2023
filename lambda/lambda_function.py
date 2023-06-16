# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

import json
from ask_sdk_model.interfaces.alexa.presentation.apl import (
    RenderDocumentDirective)

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

from roomFunctions import get_rooms, check_answer

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #speak_output =  f"Welcome to cake time. " \
        #    f"I'll tell you a celebrity name and you try " \
        #    f"to guess the month and year they were born. " \
        #    f"See how many you can get! " \
        #    f"Would you like to play?"
            
        speak_output =  f"bienvenido a secretos familiares. " \
            f"Soy la medium Madame alexa y puedo comunicarme con " \
            f"tus ancestros, ellos hablan a traves mio y responderan tus preguntas " \
            f"y así encontraras la llave al tesoro! " \
            f"¿quieres jugar?"

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
                        "Title": 'Di "Si."',
                        "Subtitle": 'Y habla con tus ancestros.',
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


class PlayGameHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
    # type: (HandlerInput) -> bool

        return (
        ask_utils.is_request_type("IntentRequest")(handler_input)
            and ask_utils.is_intent_name("AMAZON.YesIntent")(handler_input)
        )

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #speak_output =  f"Welcome to the Yes handler."
        
        #from celebrityFunctions import get_random_celeb
        #celeb = get_random_celeb()
        #title = celeb["name"]
        #speak_output =  f'In what month and year was {celeb["name"]} born?'
        
        
        
        # get the current session attributes, creating an object you can read/update
        session_attributes = handler_input.attributes_manager.session_attributes
        
        # check if there's a current celebrity. If so, repeat the question and exit.
#        if 'current_celeb' in session_attributes.keys() and session_attributes["current_celeb"] != None:

#            speak_output = f'In what month and year was {session_attributes["current_celeb"]["name"]} born?'
#            return (
#                handler_input.response_builder
#                    .speak(speak_output)
#                    .ask(speak_output)
#                    .response☺
#                )

# Check for past celebrities array and create it if not available
#if 'past_celebs' not in session_attributes.keys():
#    session_attributes["past_celebs"] = []

        #Activate the funtion that handles the json of ancestors to get an ancestor
        from ancestorsFuntions import get_ancestor
        ancestor = get_ancestor(0)
        nameAncestor = ancestor["nombre"]
        
        
        
            
        
        
        # set the "current_ancestor" attribute in the session_attribute to have access to it in other handlers
        session_attributes["current_ancestor"] = ancestor
        # save the session attributes
        handler_input.attributes_manager.session_attributes = session_attributes
        
        #speak to the player and tells him about the first ancestor to play with
        speak_output = f'Esta bien, ahora estoy conectando con tu {ancestor["parentesco"]}, {ancestor["nombre"]}, que quieres hacer?'
        #speak_output = "<speak><voice name='Miguel'><lang xml:lang='es-US'>te quiero contar un secreto </lang></voice><speak>"
        #speak_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>Your secret is safe with me!</lang></voice></speak>"
        #speak_output = "<speak><voice name='Enrique'><lang xml:lang='es-ES'>te quiero contar un secreto </lang></voice></speak>"
        
        

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
                        "Title": nameAncestor,
                        "Subtitle": 'Que quieres preguntarle?',
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




class GetAnswerOneIntentHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
    # type: (HandlerInput) -> bool

        #return (
        #ask_utils.is_request_type("IntentRequest")(handler_input)
        #    and ask_utils.is_intent_name("GetAnswerOne")(handler_input)
        #)
        
        
        return ask_utils.is_intent_name("GetAnswerOneIntent")(handler_input)
        
        

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        
        
        
        
        
        # get the current session attributes, creating an object you can read/update
        session_attributes = handler_input.attributes_manager.session_attributes
        
        
        # check if there's a current celebrity. If so, repeat the question and exit.
#        if 'current_celeb' in session_attributes.keys() and session_attributes["current_celeb"] != None:

#            speak_output = f'In what month and year was {session_attributes["current_celeb"]["name"]} born?'
#            return (
#                handler_input.response_builder
#                    .speak(speak_output)
#                    .ask(speak_output)
#                    .response
#                )

        # Check for past celebrities array and create it if not available
        #if 'past_celebs' not in session_attributes.keys():
        #    session_attributes["past_celebs"] = []

        #Activate the funtion that handles the json of ancestors to get an ancestor
        cAnswer = session_attributes["current_ancestor"]["respuesta1"]
        ancVoice = session_attributes["current_ancestor"]["voz"]
        
        nameAncestor = session_attributes["current_ancestor"]["nombre"]     
        
        
        #speak to the player and tells him about the first ancestor to play with
        #speak_output = f'{cAnswer}'
        speak_output = f"<speak> {ancVoice} {cAnswer} </lang></voice></speak>"
         
        
        
        

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
                        "Title": nameAncestor,
                        "Subtitle": 'Que te esta diciendo?',
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




class GetCurrentAncestorIntentHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
    # type: (HandlerInput) -> bool

        #return (
        #ask_utils.is_request_type("IntentRequest")(handler_input)
        #    and ask_utils.is_intent_name("GetAnswerOne")(handler_input)
        #)
        
        
        return ask_utils.is_intent_name("GetCurrentAncestorIntent")(handler_input)
        
        

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        
        
        
        
        
        # get the current session attributes, creating an object you can read/update
        session_attributes = handler_input.attributes_manager.session_attributes
        
        
        # check if there's a current celebrity. If so, repeat the question and exit.
#        if 'current_celeb' in session_attributes.keys() and session_attributes["current_celeb"] != None:

#            speak_output = f'In what month and year was {session_attributes["current_celeb"]["name"]} born?'
#            return (
#                handler_input.response_builder
#                    .speak(speak_output)
#                    .ask(speak_output)
#                    .response
#                )

        # Check for past celebrities array and create it if not available
        #if 'past_celebs' not in session_attributes.keys():
        #    session_attributes["past_celebs"] = []

        #Activate the funtion that handles the json of ancestors to get an ancestor
        cAncestorName = session_attributes["current_ancestor"]["nombre"]
        cAncestorRelation = session_attributes["current_ancestor"]["parentesco"]
        ancVoice = session_attributes["current_ancestor"]["voz"]
        
        #nameAncestor = session_attributes["current_ancestor"]["nombre"]     
        
        
        #speak to the player and tells him about the first ancestor to play with
        speak_output = f"<speak> {ancVoice} soy {cAncestorName} y soy tu {cAncestorRelation} </lang></voice></speak>"
         
        
        
        

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
                        "Title": cAncestorName,
                        "Subtitle": 'Que te esta diciendo?',
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




class GetNearRelativesIntentHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
    # type: (HandlerInput) -> bool

        #return (
        #ask_utils.is_request_type("IntentRequest")(handler_input)
        #    and ask_utils.is_intent_name("GetAnswerOne")(handler_input)
        #)
        
        
        return ask_utils.is_intent_name("GetNearRelativesIntent")(handler_input)
        
        

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        
        
        
        
        
        # get the current session attributes, creating an object you can read/update
        session_attributes = handler_input.attributes_manager.session_attributes
        
        ancestor = session_attributes["current_ancestor"]
        
        #bring the funtion to read ancestors from the json
        from ancestorsFuntions import get_ancestor
        
        arrayConexiones = ancestor["conexiones"]
        arrayRelatives = []
        
        
        #Toma los valores de la conexiónes del ancestro presente y revisa si tiene conyuge, padre, madre e hija(o) en ese orden. los coloca en una variable.
        numeroPrueba = arrayConexiones[0]
        if numeroPrueba>0:
            arrayRelatives.append(get_ancestor(numeroPrueba-1))
        
        numeroPrueba = arrayConexiones[1]
        if numeroPrueba>0:
            arrayRelatives.append(get_ancestor(numeroPrueba-1))
            
        numeroPrueba = arrayConexiones[2]
        if numeroPrueba>0:
            arrayRelatives.append(get_ancestor(numeroPrueba-1))
        
        numeroPrueba = arrayConexiones[3]
        if numeroPrueba>0:
            arrayRelatives.append(get_ancestor(numeroPrueba-1))
        
        
        #speak to the player and tells him about the first ancestor to play with
        #speak_output = f'soy {cAncestorName} y soy tu {cAncestorRelation}'
        
        numeroTamaño = len(arrayRelatives)
        
        #ahora dependiendo del numero de conexiones presenta a los parientes que estan conectados a el ancestro actual 
        if numeroTamaño == 1:
            speak_output = f'aqui en este cuarto tambien esta {arrayRelatives[0]["nombre"]} tu {arrayRelatives[0]["parentesco"]}'
        
        elif numeroTamaño == 2:
            speak_output = f'aqui en este cuarto tambien estan {arrayRelatives[0]["nombre"]} tu {arrayRelatives[0]["parentesco"]} y {arrayRelatives[1]["nombre"]} tu {arrayRelatives[1]["parentesco"]}'
        
        elif numeroTamaño == 3:
            speak_output = f'aqui en este cuarto tambien estan {arrayRelatives[0]["nombre"]} tu {arrayRelatives[0]["parentesco"]}, {arrayRelatives[1]["nombre"]} tu {arrayRelatives[1]["parentesco"]},  y {arrayRelatives[2]["nombre"]} tu {arrayRelatives[2]["parentesco"]}'
            
        elif numeroTamaño == 4:
            speak_output = f'aqui en este cuarto tambien estan {arrayRelatives[0]["nombre"]} tu {arrayRelatives[0]["parentesco"]}, {arrayRelatives[1]["nombre"]} tu {arrayRelatives[1]["parentesco"]},  {arrayRelatives[2]["nombre"]} tu {arrayRelatives[2]["parentesco"]}, y {arrayRelatives[3]["nombre"]} tu {arrayRelatives[3]["parentesco"]}'
        
        else:
            speak_output = f'aqui en este cuarto no hay nadie mas'
            
        
        
        

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
                        "Title": 'en contruccion',
                        "Subtitle": 'Perdone las molestias',
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


class TalkToAnotherAncestorIntentHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
    # type: (HandlerInput) -> bool

        #return (
        #ask_utils.is_request_type("IntentRequest")(handler_input)
        #    and ask_utils.is_intent_name("GetAnswerOne")(handler_input)
        #)
        
        
        return ask_utils.is_intent_name("TalkToAnotherAncestorIntent")(handler_input)
        
        

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        

        # get the current session attributes, creating an object you can read/update
        session_attributes = handler_input.attributes_manager.session_attributes
        
        ancestor = session_attributes["current_ancestor"]
        
        #bring the funtion to read ancestors from the json
        from ancestorsFuntions import get_ancestor
        
        
        arrayConexiones = ancestor["conexiones"]
        arrayRelatives = []
        
        
        #Toma los valores de la conexiónes del ancestro presente y revisa si tiene conyuge, padre, madre e hija(o) en ese orden. los coloca en una variable.
        numeroPrueba = arrayConexiones[0]
        if numeroPrueba>0:
            arrayRelatives.append(get_ancestor(numeroPrueba-1))
        
        numeroPrueba = arrayConexiones[1]
        if numeroPrueba>0:
            arrayRelatives.append(get_ancestor(numeroPrueba-1))
            
        numeroPrueba = arrayConexiones[2]
        if numeroPrueba>0:
            arrayRelatives.append(get_ancestor(numeroPrueba-1))
        
        numeroPrueba = arrayConexiones[3]
        if numeroPrueba>0:
            arrayRelatives.append(get_ancestor(numeroPrueba-1))
        
        #Here you recognize the person teh player is asking you about.
        relative = ask_utils.request_util.get_slot(handler_input, "familiar").value
        
        
        
        number2SwitchRelative = 0
        isRelativeHere = False
        for xFamiliar in arrayRelatives:
            if xFamiliar["parentesco"] == relative:
                isRelativeHere = True
                
                number2SwitchRelative = xFamiliar["id"]
                number2SwitchRelative = number2SwitchRelative-1
                
                session_attributes["current_ancestor"] = get_ancestor(number2SwitchRelative)
                ancestor = session_attributes["current_ancestor"]
                
            
        #speak to the player and tells him that she is switching relatives if this relative is near
        if isRelativeHere == True:
            #speak_output = f'entiendo, canalizando a tu {ancestor["parentesco"]}, mmmmm, ahora estas hablando con {ancestor["nombre"]} tu {ancestor["parentesco"]}'
            speak_output = f'<speak> entiendo, canalizando a tu {ancestor["parentesco"]}, <audio src="soundbank://soundlibrary/bell/chimes/chimes_08"/>, ahora estas hablando con {ancestor["nombre"]} tu {ancestor["parentesco"]}</speak>'
        
        else:
            speak_output = f'Lo siento, Aqui no esta ese familiar'
         
          
        
        #speak_output = f' el valor de isRelativeHere es {isRelativeHere}, y el de number2SwitchRelative es {number2SwitchRelative}'
        
        
        
        

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
                        "Title": 'en contruccion',
                        "Subtitle": 'Perdone las molestias',
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


class GuessKeyLocationIntentHandler(AbstractRequestHandler):
    """Handler para intentar adivinar la localizacion de la llave"""
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        logger.info("In GuessKeyLocationIntentHandler.can_handle")
        
        result = ask_utils.is_request_type("IntentRequest")(handler_input) and ask_utils.is_intent_name("GuessKeyLocationIntent")(handler_input)
        
        logger.info(f"GuessKeyLocationIntentHandler.can_handle = {result}")
        
        return result
        # return ask_utils.is_intent_name("GuessKeyLocationIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        logger.info("In GuessKeyLocationIntentHandler.handle")
        
        # get the slot values
        location = None
        slot = ask_utils.request_util.get_slot(handler_input, "location")
        if slot is not None:
            location = slot.value
        
        logger.info(f"location = {location}")
        
        if location == None:
            # If there's no room/location, assume that the player's input was the 
            # "question"
            all_rooms = get_rooms()
            logger.info(f"all_rooms = {all_rooms}")
            speak_output = f"Ok, estos son los cuartos disponibles: {all_rooms}." \
                f"Cual cuarto es?"
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
            )
            
        logger.info(f"checking answer...")
        
        # variables for our visual.
        title = ""
        subtitle = ""
        
        # if there's an answer, check it against the true option
        if check_answer(location):
            logger.info(f"success")
            # success, let the player know
            # TODO: Handle end_of_game state, so we can start again
            title = "Felicitaciones!"
            subtitle = "Bien hecho!"
            speak_output = f"Asi es!  La llave esta en {location}.  " \
                f"El capitulo 2 de esta aventura estara disponible en GGJ 2024 😉"
        else:
            logger.info(f"failure")
            # not the correct one.
            title = "Hmmm, 🤔!"
            subtitle = "Quieres intentar de nuevo?"
            speak_output = f"Esa no es la ubicacion de la llave. Quieres intentar de nuevo?"

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
                        "Title": title,
                        "Subtitle": subtitle,
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
        
        
        
class GetAnswerTwoIntentHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
    # type: (HandlerInput) -> bool

        #return (
        #ask_utils.is_request_type("IntentRequest")(handler_input)
        #    and ask_utils.is_intent_name("GetAnswerOne")(handler_input)
        #)
        
        
        return ask_utils.is_intent_name("GetAnswerTwoIntent")(handler_input)
        
        

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        # get the current session attributes, creating an object you can read/update
        session_attributes = handler_input.attributes_manager.session_attributes
        
        

        # Check for past celebrities array and create it if not available
        #if 'past_celebs' not in session_attributes.keys():
        #    session_attributes["past_celebs"] = []

        #Activate the funtion that handles the json of ancestors to get an ancestor
        cAnswer2 = session_attributes["current_ancestor"]["respuesta2"]
        ancVoice = session_attributes["current_ancestor"]["voz"]
        
        nameAncestor = session_attributes["current_ancestor"]["nombre"]     
        
        
        #speak to the player and tells him about the first ancestor to play with
        #speak_output = f'{cAnswer}'
        speak_output = f"<speak> {ancVoice} {cAnswer2} </lang></voice></speak>"
         
        
        
        

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
                        "Title": nameAncestor,
                        "Subtitle": 'Que te esta diciendo?',
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



class GetAnswerThreeIntentHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
    # type: (HandlerInput) -> bool

        #return (
        #ask_utils.is_request_type("IntentRequest")(handler_input)
        #    and ask_utils.is_intent_name("GetAnswerOne")(handler_input)
        #)
        
        
        return ask_utils.is_intent_name("GetAnswerThreeIntent")(handler_input)
        
        

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        # get the current session attributes, creating an object you can read/update
        session_attributes = handler_input.attributes_manager.session_attributes
        
        

        # Check for past celebrities array and create it if not available
        #if 'past_celebs' not in session_attributes.keys():
        #    session_attributes["past_celebs"] = []

        #Activate the funtion that handles the json of ancestors to get an ancestor
        cAnswer3 = session_attributes["current_ancestor"]["respuesta3"]
        ancVoice = session_attributes["current_ancestor"]["voz"]
        
        nameAncestor = session_attributes["current_ancestor"]["nombre"]     
        
        
        #speak to the player and tells him about the first ancestor to play with
        #speak_output = f'{cAnswer}'
        speak_output = f"<speak> {ancVoice} {cAnswer3} </lang></voice></speak>"
         
        
        
        

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
                        "Title": nameAncestor,
                        "Subtitle": 'Que te esta diciendo?',
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
        


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(PlayGameHandler())
sb.add_request_handler(GetAnswerOneIntentHandler())
sb.add_request_handler(GetCurrentAncestorIntentHandler())
sb.add_request_handler(GetNearRelativesIntentHandler())
sb.add_request_handler(TalkToAnotherAncestorIntentHandler())
sb.add_request_handler(GuessKeyLocationIntentHandler())
sb.add_request_handler(GetAnswerTwoIntentHandler())
sb.add_request_handler(GetAnswerThreeIntentHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()