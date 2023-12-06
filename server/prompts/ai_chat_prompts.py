# this file contains prompts for ai chat


def ai_chat_prompts(text):
    return f"""Generate a solution or answer for the given question in depth: 
    ###
    Question: Explain the concept of molecular chirality and its significance in organic chemistry, providing an example of a chiral molecule and how its enantiomers differ in their interactions with polarized light.
    Answer: Molecular chirality refers to the non-superimposable mirror images of a molecule, known as enantiomers. In organic chemistry, this property profoundly influences biological activity and chemical reactivity. Consider the example of L- and D-glucose, both chiral forms of the sugar. While these enantiomers share identical physical properties, they rotate plane-polarized light in opposite directions due to their mirror-image nature. This optical activity is crucial in pharmaceuticals and biological processes, as only one enantiomer may interact effectively with specific receptors, emphasizing the critical role of chirality in drug design and understanding molecular behavior.
    ###
    Question: What do you think is the most significant technological advancement of the past decade, and how has it impacted society?
    Answer: The advent of widespread artificial intelligence (AI) is arguably the most significant technological advancement of the past decade. AI has revolutionized industries like healthcare, finance, and transportation, streamlining processes and enhancing efficiency. Its integration into daily life through virtual assistants and smart devices has reshaped how we interact with technology. However, concerns about privacy, ethics, and job displacement have also arisen. Overall, AI's impact on society is profound, reshaping industries and daily activities while prompting discussions on its responsible and ethical deployment.
    ###
    Question: What are some key challenges and potential solutions for addressing income inequality in contemporary society?
    Answer: Income inequality poses a multifaceted challenge, driven by factors like globalization, technological shifts, and systemic biases. Challenges include disparities in education, limited access to opportunities, and unequal distribution of wealth. Solutions encompass progressive taxation, enhanced education accessibility, and social welfare reforms. Implementing fair labor practices, promoting gender and racial equity, and fostering inclusive economic policies are crucial. Additionally, investing in skill development and supporting small businesses can mitigate disparities. Tackling income inequality requires a comprehensive, interdisciplinary approach, involving policymakers, businesses, and communities to create a more just and equitable society.
    ###
    Question: {text}
    Answer:"""