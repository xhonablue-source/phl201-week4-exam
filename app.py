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
    # Continue with remaining 40 questions...
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
    # Add remaining questions 13-50 following the same pattern...
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
        
