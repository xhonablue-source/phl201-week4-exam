import streamlit as st

# Page config
st.set_page_config(page_title="Philosophy of Mind Quiz", page_icon="🧠", layout="wide")

# Initialize session state
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Questions data
questions = [
    {
        "id": 1,
        "question": "According to Sartre, what does human freedom imply about our choices?",
        "options": [
            "We are free to choose but not responsible for outcomes",
            "When we choose, we imply everyone should choose the same",
            "Freedom means we can avoid making choices",
            "Our choices are determined by God"
        ],
        "correct": 1,
        "explanation": "Sartre argues that when we choose something, we imply it is good and ought to be chosen, making us responsible not only for our own choices but for what we imply everyone should choose."
    },
    {
        "id": 2,
        "question": "What is Sartre's conclusion about God's existence?",
        "options": [
            "God exists and guides our choices",
            "God's existence is uncertain",
            "God does not exist",
            "God exists but is indifferent to humans"
        ],
        "correct": 2,
        "explanation": "Sartre explicitly states that God does not exist, and therefore we are alone with no divine guidance for our choices."
    },
    {
        "id": 3,
        "question": "According to Sartre, what does 'anguish' mean?",
        "options": [
            "Physical pain from difficult decisions",
            "Fear of death",
            "Recognition of our total and deep responsibility when choosing",
            "Uncertainty about the future"
        ],
        "correct": 2,
        "explanation": "Anguish refers to the realization that we bear complete responsibility not just for ourselves but for what everyone ought to choose."
    },
    {
        "id": 4,
        "question": "What does Sartre mean by 'abandonment'?",
        "options": [
            "Being left alone by friends",
            "God does not exist and we face all consequences alone",
            "Losing hope in humanity",
            "Being rejected by society"
        ],
        "correct": 1,
        "explanation": "Abandonment means God does not exist, so we are alone and must face all consequences of our choices without divine rescue or guidance."
    },
    {
        "id": 5,
        "question": "According to Sartre, what is 'despair'?",
        "options": [
            "Losing all hope for the future",
            "Confining ourselves to reckoning only with what depends on our will",
            "Giving up on making choices",
            "Accepting that life is meaningless"
        ],
        "correct": 1,
        "explanation": "Despair means we can only reckon with what depends on our own will—we cannot adapt the world to our desires or rely on external forces."
    },
    {
        "id": 6,
        "question": "In Sartre's view, what defines a human being?",
        "options": [
            "Their genetic makeup",
            "The sum of their actions",
            "Their intentions and beliefs",
            "Their social relationships"
        ],
        "correct": 1,
        "explanation": "Sartre claims each human being is 'nothing else but the sum of his actions'—we are what we do, not what we intend or plan."
    },
    {
        "id": 7,
        "question": "In Plato's Phaedo, what does Socrates say the soul resembles?",
        "options": [
            "The body",
            "Water",
            "Something divine, immortal, and intelligible",
            "A material object"
        ],
        "correct": 2,
        "explanation": "Socrates argues the soul resembles what is divine, immortal, intelligible, uniform, indissoluble, and unchangeable."
    },
    {
        "id": 8,
        "question": "According to Plato, what happens to a soul that becomes 'polluted'?",
        "options": [
            "It becomes stronger",
            "It is dragged down to the visible world after death",
            "It immediately dies",
            "It gains wisdom"
        ],
        "correct": 1,
        "explanation": "Plato argues that a soul polluted by bodily desires becomes heavy and is dragged down to wander among tombs and sepulchers after death."
    },
    {
        "id": 9,
        "question": "What is Plato's view on the relationship between soul and body?",
        "options": [
            "They are equal partners",
            "The soul should rule over the body",
            "The body should control the soul",
            "They are identical"
        ],
        "correct": 1,
        "explanation": "Plato argues the 'pure' soul should rule over the 'impure' body, turning away from bodily desires and wild passions."
    },
    {
        "id": 10,
        "question": "According to the rationalistic view, what is the essential characteristic of human nature?",
        "options": [
            "Emotion",
            "Physical strength",
            "Reason",
            "Social connection"
        ],
        "correct": 2,
        "explanation": "The rationalistic view claims reason is the essential characteristic of human nature that distinguishes humans from other beings."
    },
    {
        "id": 11,
        "question": "In the rationalistic view, who possesses full reason?",
        "options": [
            "All humans equally",
            "Only adult men",
            "Only philosophers",
            "Only the educated"
        ],
        "correct": 1,
        "explanation": "The rationalistic view argues that full reason belongs only to adult men, while women are driven by emotions and desires."
    },
    {
        "id": 12,
        "question": "What do feminist critics claim about the rationalistic view?",
        "options": [
            "It is completely accurate",
            "It is sexist and biased against women",
            "It needs minor adjustments",
            "It applies only to ancient times"
        ],
        "correct": 1,
        "explanation": "Feminist critics argue the rationalistic view is sexist because it claims women are not fully rational and therefore should be ruled by men."
    },
    {
        "id": 13,
        "question": "How was the rationalistic view used during colonization?",
        "options": [
            "It wasn't used at all",
            "To justify treating Native Americans as 'barbarians' who could be enslaved",
            "To promote equality",
            "To encourage cultural exchange"
        ],
        "correct": 1,
        "explanation": "Europeans used Aristotle's rationalistic claims to argue that Indigenous people were less rational 'barbarians' who could justifiably be treated like slaves."
    },
    {
        "id": 14,
        "question": "What is the mind-body problem?",
        "options": [
            "How to keep both mind and body healthy",
            "How mind and body can be so different yet interact",
            "Whether the brain is part of the body",
            "Why we have both thoughts and feelings"
        ],
        "correct": 1,
        "explanation": "The mind-body problem asks how the mind and body can be completely different from each other yet still interact and influence one another."
    },
    {
        "id": 15,
        "question": "What is consciousness according to the text?",
        "options": [
            "The ability to move",
            "Awareness of sensing, feeling, and thinking when awake",
            "Having a brain",
            "The ability to speak"
        ],
        "correct": 1,
        "explanation": "Consciousness is the awareness you have of your sensing, feeling, and thinking when you are awake—being aware that you are experiencing something."
    },
    {
        "id": 16,
        "question": "What makes consciousness 'subjective'?",
        "options": [
            "It can be measured scientifically",
            "It exists only as experienced by someone and others cannot be aware of it 'from the inside'",
            "It is the same for everyone",
            "It is purely physical"
        ],
        "correct": 1,
        "explanation": "Consciousness is subjective because it exists only to the extent that someone is experiencing it, and others cannot be aware of your consciousness 'from the inside.'"
    },
    {
        "id": 17,
        "question": "What is dualism in philosophy of mind?",
        "options": [
            "The view that there are two gods",
            "The view that humans consist of two different kinds of things: mind and body",
            "The view that there are two types of bodies",
            "The view that consciousness has two parts"
        ],
        "correct": 1,
        "explanation": "Dualism is the view that humans consist of a physical body and a nonphysical or immaterial mind, two completely different kinds of things."
    },
    {
        "id": 18,
        "question": "Who was the first great philosopher of the modern age to propose a clear version of mind-body dualism?",
        "options": [
            "Plato",
            "Aristotle",
            "René Descartes",
            "David Hume"
        ],
        "correct": 2,
        "explanation": "René Descartes (1596-1650) was the first philosopher of the modern age to propose a much clearer version of the Traditional view that our minds are different from our bodies."
    },
    {
        "id": 19,
        "question": "What were Descartes' four rules for discovering truth?",
        "options": [
            "Pray, meditate, study, reflect",
            "Accept nothing unclear, divide difficulties, carry on reflections in order, make complete enumerations",
            "Question everything, trust no one, seek evidence, remain skeptical",
            "Observe, hypothesize, test, conclude"
        ],
        "correct": 1,
        "explanation": "Descartes' rules were: accept nothing not clearly true, divide difficulties into parts, carry on reflections in due order from simple to complex, and make enumerations so complete nothing is omitted."
    },
    {
        "id": 20,
        "question": "What famous conclusion did Descartes reach on November 10, 1619?",
        "options": [
            "God exists",
            "The body and mind are separate",
            "I think, therefore I am",
            "Everything is an illusion"
        ],
        "correct": 2,
        "explanation": "Descartes concluded 'I think, therefore I am' was so certain and assured that even the most extravagant suppositions of the skeptics were incapable of shaking it."
    },
    {
        "id": 21,
        "question": "According to Descartes, can you conceive of yourself without a body?",
        "options": [
            "No, it's impossible",
            "Yes, but not without a thinking mind",
            "Only in dreams",
            "Only after death"
        ],
        "correct": 1,
        "explanation": "Descartes argues he can conceive of himself without a body, but he cannot conceive of himself without a thinking mind. Therefore, he is essentially a thinking mind, not a body."
    },
    {
        "id": 22,
        "question": "What crucial assumption does Descartes make about conceivability?",
        "options": [
            "If you can conceive of one thing without another, they must be different",
            "Conceiving something makes it real",
            "What you cannot conceive doesn't exist",
            "Conceivability proves immortality"
        ],
        "correct": 0,
        "explanation": "Descartes assumes that if we can conceive of one thing without the other, then those two things are different; if we can't, then one must be an essential part of the other."
    },
    {
        "id": 23,
        "question": "How does Descartes describe the body?",
        "options": [
            "As a spiritual entity",
            "As something that can be defined by shape, place, and space",
            "As identical to the mind",
            "As an illusion"
        ],
        "correct": 1,
        "explanation": "Descartes describes the body as something that can be confined in place, can fill space, can be perceived by senses, and can be moved—all physical, material properties."
    },
    {
        "id": 24,
        "question": "What is Descartes' view of human nature called?",
        "options": [
            "Monism",
            "Materialism",
            "Dualism",
            "Idealism"
        ],
        "correct": 2,
        "explanation": "Descartes' view is called dualism because it claims humans are made up of dual (two) kinds of substances: a material body and an immaterial mind."
    },
    {
        "id": 25,
        "question": "According to Descartes, what are you essentially?",
        "options": [
            "Your physical body",
            "Your breathing and movement",
            "Your conscious thinking mind",
            "A combination of mind and body equally"
        ],
        "correct": 2,
        "explanation": "Descartes concludes that you are, strictly speaking, only your thinking conscious mind, not your breathing, extended body."
    },
    {
        "id": 26,
        "question": "What is behaviorism's main claim about the mind?",
        "options": [
            "The mind is a separate substance",
            "The mind is how you behave",
            "The mind doesn't exist",
            "The mind is the soul"
        ],
        "correct": 1,
        "explanation": "Behaviorism argues that the mind should be explained as observable external behavior, not as internal consciousness or mental states."
    },
    {
        "id": 27,
        "question": "Who was the major advocate of behaviorism?",
        "options": [
            "René Descartes",
            "Gilbert Ryle",
            "John Searle",
            "David Chalmers"
        ],
        "correct": 1,
        "explanation": "The British philosopher Gilbert Ryle (1900-1976) was the major advocate of the behaviorist approach to the mind."
    },
    {
        "id": 28,
        "question": "What did Ryle call Descartes' view of the mind?",
        "options": [
            "The soul theory",
            "The consciousness hypothesis",
            "The dogma of the ghost in the machine",
            "The dualist error"
        ],
        "correct": 2,
        "explanation": "Ryle ridiculed Descartes' view by calling it 'the dogma of the ghost in the machine,' arguing that minds are not immaterial things (ghosts) inside physical bodies (machines)."
    },
    {
        "id": 29,
        "question": "What is a 'category mistake' according to Ryle?",
        "options": [
            "Making a mathematical error",
            "Putting things that belong to different categories on the same level",
            "Forgetting what category something belongs to",
            "Mixing up words with similar meanings"
        ],
        "correct": 1,
        "explanation": "A category mistake occurs when you put bodies and minds on the same level as if they're both individual entities, when actually 'mind' refers to behaviors or dispositions, not objects."
    },
    {
        "id": 30,
        "question": "According to Ryle, what does it mean to say 'John knows what chairs are'?",
        "options": [
            "John has a mental image of chairs in his mind",
            "John is disposed to behave in certain ways with chairs",
            "John has studied chairs scientifically",
            "John owns many chairs"
        ],
        "correct": 1,
        "explanation": "Ryle argues this means John is disposed to engage in certain specific behaviors with chairs, not that he has some internal mental object."
    },
    {
        "id": 31,
        "question": "What is the main problem with behaviorism according to critics?",
        "options": [
            "It's too complicated",
            "It reduces the mind to observable behavior, leaving out interior consciousness",
            "It contradicts science",
            "It's too old-fashioned"
        ],
        "correct": 1,
        "explanation": "Critics argue behaviorism leaves out what is most important: our interior conscious states like feelings of pleasure, pain, and happiness that may not show in behavior."
    },
    {
        "id": 32,
        "question": "What example do critics use to show behaviorism's weakness?",
        "options": [
            "A sleeping person",
            "A 'superactor' who perfectly imitates pain without feeling it",
            "A robot",
            "A person with amnesia"
        ],
        "correct": 1,
        "explanation": "Critics imagine a 'superactor' who behaves exactly like someone in pain but feels nothing, or a 'superspartan' who endures pain without showing it—proving behavior doesn't equal mental states."
    },
    {
        "id": 33,
        "question": "What is functionalism's main claim?",
        "options": [
            "The mind is a separate substance",
            "Mental activities can be explained as connections between sensory inputs and behavior outputs",
            "Only behavior matters",
            "The mind is identical to the brain"
        ],
        "correct": 1,
        "explanation": "Functionalism holds that we can explain mental activities and states as the connections between our sense 'inputs' and behavior 'outputs' and other mental states."
    },
    {
        "id": 34,
        "question": "According to functionalism, what is a belief?",
        "options": [
            "A brain state",
            "A behavior",
            "A connection the brain makes between certain sense inputs and certain behavior outputs",
            "An immaterial entity"
        ],
        "correct": 2,
        "explanation": "Functionalism explains beliefs as whatever connections the brain makes between sensory inputs and behavior outputs, focusing on the function rather than the substance."
    },
    {
        "id": 35,
        "question": "Who were key developers of functionalism?",
        "options": [
            "Plato and Aristotle",
            "Hilary Putnam, Jerry Fodor, and David Armstrong",
            "Descartes and Spinoza",
            "Kant and Hegel"
        ],
        "correct": 1,
        "explanation": "Functionalism was developed by American philosophers Hilary Putnam (1926-2016) and Jerry Fodor (1935-2017), and Australian philosopher David M. Armstrong (1926-2014)."
    },
    {
        "id": 36,
        "question": "What analogy is often used to explain the functionalist view of mind?",
        "options": [
            "Mind is like water",
            "Mind is like a ghost",
            "Mind is like a computer",
            "Mind is like a book"
        ],
        "correct": 2,
        "explanation": "Some functionalists argue that the brain is like a computer—it processes inputs (sense perceptions) and generates outputs (behaviors), with mental states as the functional connections."
    },
    {
        "id": 37,
        "question": "What is the main criticism of functionalism?",
        "options": [
            "It's too simple",
            "It leaves out inner conscious states we're directly aware of",
            "It contradicts dualism",
            "It relies too heavily on technology"
        ],
        "correct": 1,
        "explanation": "Critics argue functionalism leaves out our inner consciousness and inner sense experiences—what it feels like to have subjective experiences from the inside."
    },
    {
        "id": 38,
        "question": "What thought experiment do critics use against functionalism?",
        "options": [
            "The dream argument",
            "Two people experiencing colors differently but sorting them identically",
            "The brain in a vat",
            "The zombie apocalypse"
        ],
        "correct": 1,
        "explanation": "Critics imagine two people who experience colors completely differently but produce the same behavioral outputs, showing that identical functions don't mean identical conscious experiences."
    },
    {
        "id": 39,
        "question": "What is the identity theory of mind?",
        "options": [
            "Mind and body are identical",
            "Mental states are simply identical with states of the brain",
            "All minds are identical",
            "Identity is a mental construct"
        ],
        "correct": 1,
        "explanation": "The identity theory claims that mental states like thinking or feeling pain are simply identical with states of the brain—they're the same thing, not two different things."
    },
    {
        "id": 40,
        "question": "Who developed the identity theory?",
        "options": [
            "Descartes",
            "J.J.C. Smart",
            "Gilbert Ryle",
            "John Locke"
        ],
        "correct": 1,
        "explanation": "The Australian philosopher J.J.C. Smart (1920-2012) developed the identity theory, claiming that mental states are brain states."
    },
    {
        "id": 41,
        "question": "What does Smart mean when he says sensations are 'nothing over and above brain processes'?",
        "options": [
            "Sensations don't exist",
            "Sensations are reports of brain processes, not separate entities",
            "Brain processes cause sensations",
            "Sensations and brain processes are correlated"
        ],
        "correct": 1,
        "explanation": "Smart argues that saying you have a sensation is just reporting that a brain process is happening—the sensation is the brain process, not something extra."
    },
    {
        "id": 42,
        "question": "Why does Smart believe mental states must be physical?",
        "options": [
            "Because the Bible says so",
            "Because it seems 'frankly unbelievable' that they could be non-physical",
            "Because experiments prove it",
            "Because philosophers agree"
        ],
        "correct": 1,
        "explanation": "Smart argues he 'just cannot believe' mental states are 'something irreducibly psychical' because science has been so successful at reducing everything else to physical processes."
    },
    {
        "id": 43,
        "question": "What is Smart's argument about nonphysical entities and evolution?",
        "options": [
            "Evolution proves dualism is correct",
            "Nonphysical properties could not arise through biochemical evolution",
            "Evolution created the soul",
            "Physical and nonphysical evolved separately"
        ],
        "correct": 1,
        "explanation": "Smart argues that all human capacities evolved from physical capacities through biochemical processes, so nonphysical things cannot be produced from physical things."
    },
    {
        "id": 44,
        "question": "What is the main criticism of Smart's identity theory?",
        "options": [
            "It's too complicated",
            "Mental states and brain states have very different qualities and so cannot be identical",
            "It contradicts behaviorism",
            "It's scientifically proven wrong"
        ],
        "correct": 1,
        "explanation": "Critics argue that conscious experiences (which have no location, color, or shape) and brain states (which are physically observable) have such different qualities they cannot be the same thing."
    },
    {
        "id": 45,
        "question": "What is John Searle's 'Chinese Room' argument about?",
        "options": [
            "Learning languages",
            "A person following rules can pass the Turing Test without understanding Chinese",
            "Chinese philosophy",
            "Room design"
        ],
        "correct": 1,
        "explanation": "Searle's Chinese Room shows that someone can follow a program to produce correct Chinese responses without understanding Chinese, proving that following a program doesn't equal consciousness."
    },
    {
        "id": 46,
        "question": "What does Searle's Chinese Room argument demonstrate?",
        "options": [
            "Computers are conscious",
            "Following a program does not equal having consciousness or understanding",
            "Chinese is impossible to learn",
            "The Turing Test is perfect"
        ],
        "correct": 1,
        "explanation": "Searle argues that a computer following a program doesn't have consciousness or understanding of meaning, even if it passes the Turing Test."
    },
    {
        "id": 47,
        "question": "What is eliminative materialism?",
        "options": [
            "The view that only physical things exist",
            "The view that our ordinary conceptions of mind are false and should be eliminated",
            "The view that we should eliminate the body",
            "The view that consciousness doesn't exist"
        ],
        "correct": 1,
        "explanation": "Eliminative materialism claims our commonsense views about minds (folk psychology) are fundamentally mistaken and should be replaced by neuroscience."
    },
    {
        "id": 48,
        "question": "Who advocates eliminative materialism?",
        "options": [
            "Descartes",
            "Paul Churchland",
            "Plato",
            "Aristotle"
        ],
        "correct": 1,
        "explanation": "Canadian philosopher Paul Churchland (1942-) calls our ordinary views about minds 'folk psychology' and argues this antiquated theory should be eliminated."
    },
    {
        "id": 49,
        "question": "What is David Chalmers' 'zombie' argument about?",
        "options": [
            "Horror movies",
            "We can conceive of beings physically identical to us but without consciousness",
            "Sleep deprivation",
            "Brain death"
        ],
        "correct": 1,
        "explanation": "Chalmers argues we can conceive of 'zombies' that are physically identical to us but lack consciousness, proving consciousness must be a nonphysical property."
    },
    {
        "id": 50,
        "question": "What is property dualism?",
        "options": [
            "The view that there are two types of property",
            "The view that there are two kinds of properties (physical and mental) but not two kinds of substances",
            "The view that property is divided between mind and body",
            "The view that consciousness is property"
        ],
        "correct": 1,
        "explanation": "Property dualism holds that while there's only one kind of substance (physical), consciousness is a nonphysical property that our world has—similar to how we look and act but without consciousness."
    }
]

# Header
st.title("🧠 Philosophy of Mind - Comprehensive Quiz")
st.markdown("**By Xavier Honablue M.Ed for CognitiveCloud.ai**")

# Resources Section
with st.expander("📚 Additional Resources"):
    st.markdown("""
    ### External Philosophy Resources
    
    For deeper exploration of the topics covered in this quiz, visit:
    
    - **[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)** - Comprehensive, peer-reviewed articles on philosophy topics
    - [Mind-Body Problem](https://plato.stanford.edu/entries/dualism/)
    - [Consciousness](https://plato.stanford.edu/entries/consciousness/)
    - [Functionalism](https://plato.stanford.edu/entries/functionalism/)
    - [Behaviorism](https://plato.stanford.edu/entries/behaviorism/)
    - [Descartes](https://plato.stanford.edu/entries/descartes/)
    
    *Links open in a new tab and won't affect your quiz progress*
    """, unsafe_allow_html=True)

st.info("📋 **Instructions:** Answer all questions before submitting. You can review explanations after completing the entire quiz.")

# Display questions
if not st.session_state.submitted:
    st.markdown("---")
    
    for idx, q in enumerate(questions):
        st.markdown(f"### Question {idx + 1}")
        st.write(q["question"])
        
        answer = st.radio(
            "Select your answer:",
            options=range(len(q["options"])),
            format_func=lambda x: q["options"][x],
            key=f"q_{q['id']}",
            index=st.session_state.answers.get(q['id'], None)
        )
        
        st.session_state.answers[q['id']] = answer
        st.markdown("---")
    
    # Progress tracking
    answered = len([a for a in st.session_state.answers.values() if a is not None])
    st.progress(answered / len(questions))
    st.write(f"Questions answered: {answered} / {len(questions)}")
    
    # Submit button
    if answered == len(questions):
        if st.button("Submit Quiz", type="primary", use_container_width=True):
            st.session_state.submitted = True
            st.rerun()
    else:
        st.warning("Please answer all questions before submitting.")

# Results page
else:
    # Calculate score
    score = sum(1 for q in questions if st.session_state.answers.get(q['id']) == q['correct'])
    percentage = round((score / len(questions)) * 100)
    
    # Display score
    st.success(f"## 🎯 Quiz Results: {score} / {len(questions)} ({percentage}%)")
    
    # Show answers with explanations
    st.markdown("---")
    st.markdown("## 📝 Answer Review")
    
    for idx, q in enumerate(questions):
        user_answer = st.session_state.answers.get(q['id'])
        is_correct = user_answer == q['correct']
        
        if is_correct:
            st.success(f"### ✅ Question {idx + 1}")
        else:
            st.error(f"### ❌ Question {idx + 1}")
        
        st.write(f"**{q['question']}**")
        
        st.write(f"**Your answer:** {q['options'][user_answer]}")
        
        if not is_correct:
            st.write(f"**Correct answer:** {q['options'][q['correct']]}")
        
        st.info(f"**Explanation:** {q['explanation']}")
        st.markdown("---")
    
    # Retake button
    if st.button("🔄 Retake Quiz", type="primary", use_container_width=True):
        st.session_state.answers = {}
        st.session_state.submitted = False
        st.rerun()
