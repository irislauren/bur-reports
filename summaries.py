import streamlit as st

st.title("Biennial Update Reports")
st.selectbox("Select a pair of documents", ["Thailand BUR4 vs. Malaysia BU2", "Malaysia BUR2 vs. Malaysia BUR3"])
st.header("Generated Summaries")
ex = st.expander("Prompt")
ex.write('''Provide a detailed summary of the following text [in paragraph form].
          Make sure to include nuance that the text presents and details that would 
          be relevant for a reader to fully comprehend and understand its material.''')

col1, col2 = st.columns(2)
col1.subheader("Thailand BUR4")
col2.subheader("Malaysia BU2")
col1.write('''Chapter 3 of Thailand’s Fourth Biennial Update Report provides a comprehensive overview of the country’s climate change mitigation efforts, emphasizing the integration of mitigation strategies into national and sectoral policies. The chapter focuses on the implementation of various frameworks and targets aimed at reducing greenhouse gas (GHG) emissions. Thailand’s commitment to addressing climate change is underscored by its Nationally Appropriate Mitigation Action (NAMA) and Nationally Determined Contribution (NDC) targets.

Key national plans include the 20-Year National Strategy, the Climate Change Master Plan (2015–2050), and sectoral strategies covering energy, transportation, industry, and waste management. The 20-Year National Strategy aims to achieve eco-friendly development, balancing economic, environmental, and social factors. It integrates climate action into sustainable development goals, recognizing the increasing impacts of climate change on the environment and society.

The NAMA, implemented between 2013 and 2020, achieved significant GHG reductions, especially in the energy and transport sectors. By 2020, Thailand had reduced emissions by 15.4% from the business-as-usual scenario, with renewable energy contributing the bulk of the reductions. The transition to the NDC framework represents Thailand’s second phase of climate action, targeting a 20-25% reduction by 2030, with a more ambitious long-term goal of achieving carbon neutrality by 2050 and net-zero emissions by 2065.

Thailand’s mitigation measures are diverse, spanning renewable energy promotion, energy efficiency improvements, waste management, and agricultural reforms. The report highlights the importance of technology transfer, capacity building, and international cooperation in enabling Thailand to meet its climate goals. Specific projects, such as the RAC NAMA (Refrigeration and Air Conditioning Nationally Appropriate Mitigation Action) and Thai Rice NAMA, exemplify targeted initiatives that combine policy, technology, and financial mechanisms to achieve emission reductions in key sectors.

Overall, the report illustrates Thailand’s proactive stance in climate mitigation, noting the challenges posed by limited financial and technical resources. It emphasizes the need for ongoing international support to reach the more ambitious targets outlined in the updated NDC and the Long-Term Low Greenhouse Gas Emission Development Strategy (LT-LEDS).''')

col2.write('''Chapter 3 of Malaysia’s Biennial Update Report highlights the country’s ongoing mitigation efforts to address climate change. The chapter begins by discussing how Malaysia has mainstreamed climate mitigation actions into its national development plans, particularly through the Eleventh Malaysia Plan (2016-2020), which emphasizes green growth and sustainability. It outlines key strategies aimed at climate-resilient development, resource efficiency, and sustainable energy usage.

The National Policy on Climate Change provides a framework guiding government agencies, industries, and communities toward a balanced approach to both mitigation and adaptation. This framework is based on five principles, including sustainable development, environmental conservation, and coordinated implementation of climate change actions. Additionally, the country has committed to reducing greenhouse gas (GHG) emissions intensity per GDP by 45% by 2030, based on 2005 levels.

Sectoral policies play a significant role in Malaysia’s mitigation strategy, covering energy, transport, waste management, and land-use sectors. For example, the National Renewable Energy Policy and Action Plan and the National Energy Efficiency Action Plan (NEEAP) set ambitious targets for renewable energy installation and energy efficiency improvements. In the transport sector, policies such as the National Automotive Policy and the National Electric Mobility Blueprint promote the use of electric vehicles (EVs) and biofuels, while aiming for a 40% modal share of public transport by 2030.

Waste management efforts are also prominent, with goals to increase recycling rates and reduce methane emissions from waste disposal sites. The chapter details Malaysia’s push to develop biogas facilities at palm oil mills to capture methane, which contributes to GHG reductions.

The Land Use, Land-Use Change, and Forestry (LULUCF) sector is critical for maintaining Malaysia’s carbon sink status. Policies promote sustainable forest management, ensuring that at least 50% of the country’s land remains forested, as highlighted in the REDD+ Strategy.

Finally, the chapter explores various GHG emissions projections under three scenarios: Business-as-Usual (BAU), Planning (PLAN), and Ambitious (AMB). The analysis shows that without further intervention, emissions are expected to increase, particularly from the energy sector, which will account for the majority of emissions by 2030. However, with planned and more ambitious measures, Malaysia can significantly reduce its GHG emissions by implementing aggressive energy efficiency programs and transitioning toward renewable energy.

This chapter provides a comprehensive overview of Malaysia’s policy framework, sectoral actions, and projections aimed at achieving its climate goals under the Paris Agreement and ensuring sustainable development.
''')

ex1 = st.expander("Prompt")
ex1.write('''Provide a detailed summarization by comparing the following two texts. Don't just summarize one, then the other. Make sure to include nuance that the two texts present and details that would be relevant for a reader to fully comprehend and understand their material. You shouldn't have to acknowledge the texts directly.''')

st.subheader("Thailand vs. Malaysia")
st.write('''Both Thailand and Malaysia have developed robust frameworks to mitigate climate change, though their approaches reflect their unique national circumstances, priorities, and resources. Both countries have mainstreamed climate change mitigation into their national development strategies and emphasized the importance of aligning climate action with economic growth, resource efficiency, and sustainability goals.

Thailand’s strategy is characterized by long-term planning and ambitious GHG emission reduction targets, highlighted by its 20-Year National Strategy (2018-2037) and the Climate Change Master Plan (2015-2050). These plans focus on reducing GHG emissions across key sectors, such as energy, transport, industry, and waste, while promoting low-carbon growth. Thailand’s targets include a 30-40% reduction of GHG emissions by 2030, conditional on international support for technology, finance, and capacity building . Thailand also aims for carbon neutrality by 2050 and net-zero emissions by 2065 . Thailand’s mitigation efforts incorporate both mandatory measures and voluntary actions, such as carbon market initiatives and carbon labeling schemes.

Malaysia, similarly, has adopted a green growth model as part of its Eleventh Malaysia Plan (2016-2020), which emphasizes sustainable resource management and resilience to climate change . Malaysia’s National Policy on Climate Change (2009) outlines a framework that balances mitigation and adaptation through the sustainable use of natural resources, energy efficiency, and public transportation improvements. Like Thailand, Malaysia has sectoral strategies in energy, transport, and waste management, with a focus on renewable energy, energy efficiency, and methane recovery from waste disposal  . Malaysia also commits to reducing GHG emissions intensity per GDP by 45% by 2030, relative to 2005 levels, with 10% of the reduction conditional on international support .

While both countries rely heavily on international cooperation for technological, financial, and capacity-building support, their respective plans reflect different timelines and approaches to mitigation. Thailand’s framework includes ambitious long-term targets and emphasizes the need for international support to achieve its aggressive carbon neutrality goal. Malaysia, on the other hand, frames its mitigation efforts in the context of its economic development plans and sector-specific policies, balancing the need for economic growth with environmental sustainability.

Sectorally, both countries target the energy and transport sectors as key areas for GHG reductions, promoting renewable energy and improving public transportation systems. However, Malaysia places a significant emphasis on its LULUCF (Land Use, Land-Use Change, and Forestry) sector, ensuring that 50% of the country’s land remains forested . This sector is critical for Malaysia’s carbon sink efforts, a feature less emphasized in Thailand’s mitigation plans.

Ultimately, both countries recognize the need for aggressive mitigation actions aligned with sustainable development, yet they navigate this challenge differently based on their economic structures, environmental contexts, and available resources. Both Thailand and Malaysia emphasize the importance of sectoral policies, international cooperation, and long-term strategic planning, but the depth of ambition and the specific focus areas reflect their distinct national circumstances.
''')

st.header("Generated Questions")
qcol1, qcol2 = st.columns(2)
qcol1.subheader("Thailand BUR4")
qcol2.subheader("Malaysia BU2")

thailand_qa = [
    {
        "question": "1. How does Thailand’s 20-Year National Strategy integrate climate change mitigation into sustainable development, and what challenges might arise from balancing these different objectives?",
        "answer": """**Sample Answer**: Thailand’s 20-Year National Strategy aims to balance economic, environmental, and social factors while promoting eco-friendly development. It integrates climate action by recognizing the increasing impacts of climate change on both the environment and society, thereby tying sustainable development goals with mitigation efforts. However, a challenge in balancing these objectives could arise from potential conflicts between economic growth and environmental conservation, where pursuing rapid industrial growth may hinder sustainability goals.
        \n**Where in the text**: This answer is based on the second paragraph, where the 20-Year National Strategy’s goals and the integration of climate action into sustainable development are discussed."""
    },
    {
        "question": "2. What are the key differences between Thailand’s Nationally Appropriate Mitigation Action (NAMA) and Nationally Determined Contribution (NDC), and why is the transition between them important for Thailand’s climate strategy?",
        "answer": """**Sample Answer**: The NAMA, implemented from 2013 to 2020, focused on significant reductions in greenhouse gas emissions, particularly in the energy and transport sectors, achieving a 15.4% reduction by 2020. The NDC, however, represents Thailand’s second phase of climate action, targeting more ambitious goals such as a 20-25% reduction in emissions by 2030 and achieving carbon neutrality by 2050. The transition is important because it signals a shift toward longer-term, more aggressive climate goals, reflecting Thailand’s increased commitment to addressing climate change.
        \n**Where in the text**: The third paragraph provides the details of the NAMA and NDC and explains the transition from one to the other."""
    },
]

malaysia_qa = [
    {
        "question": "1. How does the Eleventh Malaysia Plan integrate climate change mitigation into national development, and what are the key strategies outlined for achieving green growth and sustainability?",
        "answer": """**Sample Answer**: The Eleventh Malaysia Plan integrates climate change mitigation by focusing on climate-resilient development, resource efficiency, and sustainable energy usage. Key strategies include promoting green growth, enhancing sustainability, and ensuring that economic development does not compromise environmental goals. The plan also emphasizes the need for climate adaptation measures alongside mitigation efforts, helping Malaysia pursue both environmental conservation and sustainable economic development.
        \n**Where in the text**: This answer can be derived from the first paragraph, where the role of the Eleventh Malaysia Plan and its focus on green growth and sustainability are discussed."""
    }
]

with qcol1:
    for qa in thailand_qa:
        qex = st.expander(qa["question"])
        qex.write(qa["answer"])

with qcol2:
    for qa in malaysia_qa:
        qex = st.expander(qa["question"])
        qex.write(qa["answer"])

st.header("Source Documents")
st.link_button("Thailand BUR4", "https://drive.google.com/file/d/1b68cZKWcX3l7Jt5WU47Pw-EcGWFyklwe/view?usp=sharing")
st.link_button("Malaysia BU2", "https://drive.google.com/open?id=1P6aB-f0Pbkl5d01qP_mqvWGZVRkRzBK2")
st.link_button("Malaysia BUR3", "https://drive.google.com/open?id=1EAxr_FiKMORmsErR3tnXdynRWY60eLM7")