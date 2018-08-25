
def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "whatisastrofun":
        return fun_math(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello"
    speechOutput =  "Hello , Welcome to astro fun! " \
                    "You can know interesting facts about astro by saying Tell me astronomy fun"
    repromptText =  "You can know interesting facts about astro by saying Tell me astronomy fun"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def fun_math(intent, session):
    import random
    index = random.randint(0,len(prime)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Astro fact: " + prime[index] 
    repromptText = "You can know interesting facts about astronomy by saying Tell me astronomy fun"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using astro learn Alexa Skills Kit. " \
                    "Have a great time! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }



prime = [ "If the Sun were made of bananas, it would be just as hot." ,
          "All the matter that makes up the human race could fit in a sugar cube." ,
          "Events in the future can affect what happened in the past.",
          "Almost all of the Universe is missing." ,
          "Things can travel faster than light; and light doesn’t always travel very fast." ,
          "There are an infinite number of mes writing this, and an infinite number of yous reading it." ,
          "Black holes aren’t black.",
          "The fundamental description of the universe does not account for a past, present or future." ,
          "A particle here can affect one on the other side of the universe, instantaneously." ,
          "The faster you move, the heavier you get." ,
          "Neutron star can spin at a rate of 600 rotations per second.",
          "If star passes too close to a black hole it can be torn apart." ,
          "The solar system is around 4.6 billion years old. Scientists estimate that it will probably last another 5000 million years." ,
          "If you try to learn Graham's number, your brain would change into black hole." ,
          "Enceladus, one of Saturn's smaller moons, reflects some 90% of the sunlight, making it more reflrctive than snow.",
          "There's not enough space in the known universe to write out a googolplex on paper.",
          "The whirlpool galaxy(M51), was the very first celestial object to be identified as being spiral.",
          "The width of Milky Way is around 100,000 light-years.",
          "The Sun is over 300,000 times larger than Earth.",
          "Footprint and tire tracks left by astronauts on the Moon won't disappear as there is no wind to blow them away.",
          "The Sun makes full rotation once every 25-35 days." ,
          "According to mathematics, white holes are possible, although as of yet we have found none." ,
          "The only large moon in our solar system to orbit in the opposite direction of its planet is Neptune's moon, Triton." ,
          "There are more stars in space than grain of sand on earth, but there are more atoms in a grain then stars in universe." ,
          "We know more about space than deep in our oceans." ,
          "68% of universe is dark energy, and 25% is dark matter; both are invisible. This means we have seen only 5% of universe from earth." ,
          "The Space Station circles the earth every 90 minutes." ,
          "The first Supernovae observed outside of over own galaxy was the Andromeade, in the Andromeda galaxy in 1855." ,
          "On Venus, it snows metal and rains sulphuric acid." ,
          "Coca-Cola was the first drink that was ever consumed in space.",
          "The first artificial satellite in space was called 'Sputnik'." ,
          "Our moon is running away from earth at a rate of 4cm per year."
        ]
