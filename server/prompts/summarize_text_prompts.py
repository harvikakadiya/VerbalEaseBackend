# this file contains prompts for summarizer


def summarize_text_prompts(text):
    return f"""Summarize the given text: 
    ###
    Text: Global warming has presented another issue called climate change. Sometimes these phrases are used interchangeably, however, they are different. Climate change refers to changes in weather patterns and growing seasons around the world. It also refers to sea level rise caused by the expansion of warmer seas and melting ice sheets and glaciers. Global warming causes climate change, which poses a serious threat to life on Earth in the forms of widespread flooding and extreme weather. Scientists continue to study global warming and its impact on Earth.
    Summarized text: Climate change, a term often used interchangeably, refers to global warming, causing changes in weather patterns, growing seasons, and sea level rise, posing a serious threat to life on Earth through widespread flooding and extreme weather.
    ###
    Text: The great challenge in chemistry is the development of a coherent explanation of the complex behaviour of materials, why they appear as they do, what gives them their enduring properties, and how interactions among different substances can bring about the formation of new substances and the destruction of old ones. From the earliest attempts to understand the material world in rational terms, chemists have struggled to develop theories of matter that satisfactorily explain both permanence and change. The ordered assembly of indestructible atoms into small and large molecules, or extended networks of intermingled atoms, is generally accepted as the basis of permanence, while the reorganization of atoms or molecules into different arrangements lies behind theories of change. Thus chemistry involves the study of the atomic composition and structural architecture of substances, as well as the varied interactions among substances that can lead to sudden, often violent reactions.
    Summarized text: Chemistry is a complex field that focuses on understanding the behavior of materials, their properties, and interactions among substances. It involves studying atomic composition, structural architecture, and the interactions that can lead to sudden reactions. Despite attempts to rationalize the material world, chemists struggle to develop theories explaining both permanence and change.
    ###
    Text: The iPhone was first released in 2007, but at the dawn of the decade it was still a relatively niche product, confined to one wireless carrier and targeted at the early technology adopter. Now it’s a much bigger deal — in the first calendar quarter of 2010, Apple sold 8.7 million iPhones. In the first quarter of 2018, Apple sold 47 million iPhones. The iPhone has also propelled Apple. In the last 10 years, Apple has gone from a large computer company with a profitable side business in MP3 players to a $1 trillion megacorp with operations around the globe and 137,000 full-time employees. The iPhone became intertwined in our lives because it replaced so many other devices.
    Summarized text: The iPhone, launched in 2007, has transformed Apple from a niche product to a $1 trillion megacorp, selling 47 million units in Q1 2018. The iPhone has replaced many other devices, making Apple a significant player in our lives and driving Apple's growth.
    ###
    Text: {text}
    Summarized test: """