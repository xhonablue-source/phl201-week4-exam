import streamlit as st

# Page configuration
st.set_page_config(
    page_title="PHL201 Philosophy Assessment",
    page_icon="🧠",
    layout="wide"
)

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'show_resources' not in st.session_state:
    st.session_state.show_resources = False
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = 'all'

# Questions database
questions = [
    # Existentialism & Sartre (10 questions)
    {'id': 1, 'category': 'Existentialism', 'question': 'According to Sartre, what is the fundamental condition of human existence?', 'options': ['We are determined by our essence', 'We are completely free and responsible', 'We are products of our environment', 'We are governed by God\'s will'], 'correct': 1},
    {'id': 2, 'category': 'Existentialism', 'question': 'What does Sartre mean by "existence precedes essence"?', 'options': ['Humans have a predetermined nature', 'We create our own nature through choices', 'Essence is more important than existence', 'God defines our essence'], 'correct': 1},
    {'id': 3, 'category': 'Existentialism', 'question': 'What does Sartre identify as the feeling that comes with radical freedom?', 'options': ['Joy', 'Anguish', 'Contentment', 'Confusion'], 'correct': 1},
    {'id': 4, 'category': 'Existentialism', 'question': 'According to Sartre, when we choose, we also choose for:', 'options': ['Ourselves only', 'Our family', 'All humanity', 'No one else'], 'correct': 2},
    {'id': 5, 'category': 'Existentialism', 'question': 'What does Sartre mean by "abandonment"?', 'options': ['Being left alone by friends', 'God does not exist to guide us', 'Society has abandoned us', 'We abandon our responsibilities'], 'correct': 1},
    {'id': 6, 'category': 'Existentialism', 'question': 'According to Sartre, what follows from the non-existence of God?', 'options': ['Everything is permitted', 'Morality becomes objective', 'Life has inherent meaning', 'Values are absolute'], 'correct': 0},
    {'id': 7, 'category': 'Existentialism', 'question': 'Sartre claims each human being is:', 'options': ['Predetermined', 'The sum of their actions', 'Defined by society', 'Born with fixed traits'], 'correct': 1},
    {'id': 8, 'category': 'Existentialism', 'question': 'What is "despair" in Sartre\'s philosophy?', 'options': ['Clinical depression', 'Recognizing we can only control our own actions', 'Giving up on life', 'Fear of death'], 'correct': 1},
    {'id': 9, 'category': 'Existentialism', 'question': 'For Sartre, human nature is:', 'options': ['Fixed at birth', 'Created through our choices', 'Determined by genetics', 'Given by God'], 'correct': 1},
    {'id': 10, 'category': 'Existentialism', 'question': 'Sartre argues that in choosing, we create:', 'options': ['Only personal values', 'An image of what humanity should be', 'Random outcomes', 'Material wealth'], 'correct': 1},

    # Mind-Body Problem & Dualism (15 questions)
    {'id': 11, 'category': 'Mind-Body', 'question': 'What is the mind-body problem?', 'options': ['How to keep mind and body healthy', 'How immaterial mind and material body interact', 'Whether the brain exists', 'How to exercise mentally'], 'correct': 1},
    {'id': 12, 'category': 'Mind-Body', 'question': 'What is dualism in philosophy of mind?', 'options': ['Two people thinking alike', 'Mind and body are two different substances', 'Having two bodies', 'Believing in two gods'], 'correct': 1},
    {'id': 13, 'category': 'Mind-Body', 'question': 'According to Plato\'s dialogue, the soul is most like:', 'options': ['The body', 'Something divine and immortal', 'Physical matter', 'A temporary illusion'], 'correct': 1},
    {'id': 14, 'category': 'Mind-Body', 'question': 'In Plato\'s view, reason should:', 'options': ['Serve the body\'s desires', 'Rule over emotions and desires', 'Be abandoned', 'Follow passions'], 'correct': 1},
    {'id': 15, 'category': 'Mind-Body', 'question': 'What happens to a "polluted" soul according to Plato?', 'options': ['It ascends to heaven', 'It becomes divine', 'It is dragged down to earth', 'It ceases to exist'], 'correct': 2},
    {'id': 16, 'category': 'Mind-Body', 'question': 'Descartes\' famous conclusion "I think, therefore I am" establishes:', 'options': ['The body exists', 'The thinking self must exist', 'God exists', 'Nothing exists'], 'correct': 1},
    {'id': 17, 'category': 'Mind-Body', 'question': 'What did Descartes doubt in his method?', 'options': ['Only trivial things', 'Everything he could doubt', 'Nothing at all', 'Only religious beliefs'], 'correct': 1},
    {'id': 18, 'category': 'Mind-Body', 'question': 'For Descartes, the essence of the self is:', 'options': ['The body', 'Thinking/consciousness', 'Physical extension', 'Social relationships'], 'correct': 1},
    {'id': 19, 'category': 'Mind-Body', 'question': 'Descartes could conceive of himself without:', 'options': ['A thinking mind', 'A body', 'Consciousness', 'Existence'], 'correct': 1},
    {'id': 20, 'category': 'Mind-Body', 'question': 'What is consciousness according to the textbook?', 'options': ['Physical brain activity only', 'Awareness of sensing, feeling, and thinking', 'Unconscious processes', 'Bodily reflexes'], 'correct': 1},
    {'id': 21, 'category': 'Mind-Body', 'question': 'Consciousness is described as having which key feature?', 'options': ['Objectivity', 'Subjectivity and first-person nature', 'Third-person observability', 'Physical dimensions'], 'correct': 1},
    {'id': 22, 'category': 'Mind-Body', 'question': 'According to dualists, mental properties:', 'options': ['Are identical to physical properties', 'Lack physical properties like weight and color', 'Have mass and shape', 'Are observable by others'], 'correct': 1},
    {'id': 23, 'category': 'Mind-Body', 'question': 'The rationalistic view of human nature claims:', 'options': ['Emotions are superior to reason', 'Reason is the essential human characteristic', 'Humans lack reason', 'Animals are more rational than humans'], 'correct': 1},
    {'id': 24, 'category': 'Mind-Body', 'question': 'Feminist critics argue the rationalistic view:', 'options': ['Is perfectly objective', 'Is sexist against women', 'Favors emotions over reason', 'Has no historical biases'], 'correct': 1},
    {'id': 25, 'category': 'Mind-Body', 'question': 'Descartes\' first rule for finding truth was to:', 'options': ['Accept everything', 'Accept only what is clearly true', 'Trust ancient authorities', 'Believe religious texts'], 'correct': 1},

    # Behaviorism (10 questions)
    {'id': 26, 'category': 'Behaviorism', 'question': 'What is behaviorism\'s main claim about the mind?', 'options': ['Mind is immaterial substance', 'Mind is observable behavior', 'Mind doesn\'t exist', 'Mind is divine'], 'correct': 1},
    {'id': 27, 'category': 'Behaviorism', 'question': 'According to Gilbert Ryle, Descartes made what error?', 'options': ['A mathematical mistake', 'A category mistake', 'A logical proof', 'A scientific discovery'], 'correct': 1},
    {'id': 28, 'category': 'Behaviorism', 'question': 'Ryle called Descartes\' dualism:', 'options': ['The truth of the mind', 'The dogma of the ghost in the machine', 'Scientific materialism', 'Religious philosophy'], 'correct': 1},
    {'id': 29, 'category': 'Behaviorism', 'question': 'For behaviorists, "mind" refers to:', 'options': ['An immaterial substance', 'Dispositions to behave in certain ways', 'The soul', 'A separate entity'], 'correct': 1},
    {'id': 30, 'category': 'Behaviorism', 'question': 'To say someone "knows French" means they are disposed to:', 'options': ['Have a French soul', 'Behave in certain ways when given French inputs', 'Possess French matter', 'Think in a special substance'], 'correct': 1},
    {'id': 31, 'category': 'Behaviorism', 'question': 'What major criticism is raised against behaviorism?', 'options': ['It\'s too simple', 'It can\'t account for inner conscious experiences', 'It\'s too complex', 'It\'s too religious'], 'correct': 1},
    {'id': 32, 'category': 'Behaviorism', 'question': 'The "superactor" example shows behaviorism:', 'options': ['Is completely correct', 'Can\'t distinguish inner experience from behavior', 'Proves dualism', 'Explains everything'], 'correct': 1},
    {'id': 33, 'category': 'Behaviorism', 'question': 'A "superspartan" who feels pain but shows no behavior challenges:', 'options': ['Dualism', 'Behaviorism', 'Theism', 'Nihilism'], 'correct': 1},
    {'id': 34, 'category': 'Behaviorism', 'question': 'Behaviorism reduces mental states to:', 'options': ['Immaterial substances', 'Observable behaviors and dispositions', 'Divine qualities', 'Unknowable mysteries'], 'correct': 1},
    {'id': 35, 'category': 'Behaviorism', 'question': 'According to critics, behaviorism leaves out:', 'options': ['Behavior', 'Inner conscious feelings and experiences', 'Physical properties', 'Observable actions'], 'correct': 1},

    # Functionalism (12 questions)
    {'id': 36, 'category': 'Functionalism', 'question': 'What is functionalism\'s main thesis?', 'options': ['Mind is immaterial', 'Mental states are functional connections between inputs and outputs', 'Mind doesn\'t exist', 'Only behavior matters'], 'correct': 1},
    {'id': 37, 'category': 'Functionalism', 'question': 'Functionalism says mental states are defined by:', 'options': ['Their immaterial nature', 'Their function or causal role', 'Their location', 'Their color'], 'correct': 1},
    {'id': 38, 'category': 'Functionalism', 'question': 'A belief, according to functionalism, is:', 'options': ['An immaterial substance', 'Whatever connects sensory inputs to behavioral outputs in the right way', 'A physical object', 'An illusion'], 'correct': 1},
    {'id': 39, 'category': 'Functionalism', 'question': 'The computer model of mind suggests the brain is like:', 'options': ['A soul', 'A computer processing information', 'An illusion', 'A spirit'], 'correct': 1},
    {'id': 40, 'category': 'Functionalism', 'question': 'David Armstrong argued mental states must be explained in terms of:', 'options': ['Immaterial properties', 'Purely physical/materialist terms', 'Divine intervention', 'Social constructs'], 'correct': 1},
    {'id': 41, 'category': 'Functionalism', 'question': 'For functionalism, pain is:', 'options': ['A physical injury only', 'A mental state that causes distress and desire to relieve it', 'An illusion', 'A spiritual test'], 'correct': 1},
    {'id': 42, 'category': 'Functionalism', 'question': 'Functionalists believe that mental states can be caused by:', 'options': ['Only immaterial substances', 'Other mental states', 'Nothing', 'Only divine power'], 'correct': 1},
    {'id': 43, 'category': 'Functionalism', 'question': 'According to functionalism, could non-biological things have minds?', 'options': ['No, never', 'Yes, if they have the right functional organization', 'Only humans have minds', 'Only souls have minds'], 'correct': 1},
    {'id': 44, 'category': 'Functionalism', 'question': 'What major criticism is raised against functionalism?', 'options': ['It\'s too spiritual', 'It may leave out qualitative conscious experiences (qualia)', 'It\'s too simple', 'It proves dualism'], 'correct': 1},
    {'id': 45, 'category': 'Functionalism', 'question': 'The inverted spectrum problem suggests:', 'options': ['Colors don\'t exist', 'Two people with same functional states might have different experiences', 'Everyone sees the same', 'Vision is impossible'], 'correct': 1},
    {'id': 46, 'category': 'Functionalism', 'question': 'Functionalism allows that minds:', 'options': ['Must be immaterial', 'Could be realized in different materials', 'Only exist in humans', 'Are impossible'], 'correct': 1},
    {'id': 47, 'category': 'Functionalism', 'question': 'Some functionalists argue that even _____ could have a mind if properly organized:', 'options': ['Rocks', 'Computers or alien beings', 'Nothing', 'Only humans'], 'correct': 1},

    # Identity Theory (10 questions)
    {'id': 48, 'category': 'Identity Theory', 'question': 'What is the identity theory of mind?', 'options': ['Mind and body are separate', 'Mental states are identical to brain states', 'Mind is an illusion', 'Identity doesn\'t matter'], 'correct': 1},
    {'id': 49, 'category': 'Identity Theory', 'question': 'J.J.C. Smart argues mental states are:', 'options': ['Immaterial', 'Identical to physical brain processes', 'Behavioral dispositions only', 'Divine properties'], 'correct': 1},
    {'id': 50, 'category': 'Identity Theory', 'question': 'Smart believes science will discover:', 'options': ['The soul', 'Which brain states are identical to which mental states', 'That minds don\'t exist', 'That dualism is true'], 'correct': 1},
    {'id': 51, 'category': 'Identity Theory', 'question': 'For identity theorists, "having a pain" means:', 'options': ['Having an immaterial feeling', 'Being in a specific brain state', 'Behaving in pain-like ways', 'Nothing at all'], 'correct': 1},
    {'id': 52, 'category': 'Identity Theory', 'question': 'Smart\'s argument relies on the claim that:', 'options': ['Minds are immaterial', 'It\'s "frankly unbelievable" that mental states aren\'t physical', 'Science is always wrong', 'Dualism is proven'], 'correct': 1},
    {'id': 53, 'category': 'Identity Theory', 'question': 'According to Smart, nonphysical properties:', 'options': ['Are common', 'Cannot suddenly arise in evolution', 'Are the basis of mind', 'Prove dualism'], 'correct': 1},
    {'id': 54, 'category': 'Identity Theory', 'question': 'The identity theory says the mind:', 'options': ['Is the soul', 'Is the brain', 'Doesn\'t exist', 'Is separate from the body'], 'correct': 1},
    {'id': 55, 'category': 'Identity Theory', 'question': 'A major objection to identity theory is:', 'options': ['It\'s too dualistic', 'Mental states and brain states seem to have different properties', 'It proves the soul', 'It\'s too simple'], 'correct': 1},
    {'id': 56, 'category': 'Identity Theory', 'question': 'Brain states are publicly observable, but conscious experiences:', 'options': ['Are also publicly observable', 'Are private and subjective', 'Don\'t exist', 'Are identical in all ways'], 'correct': 1},
    {'id': 57, 'category': 'Identity Theory', 'question': 'Identity theory requires believing:', 'options': ['Mind and body are separate', 'Mental properties are identical to physical properties', 'The soul exists', 'Nothing is physical'], 'correct': 1},

    # Computer/Turing Test (8 questions)
    {'id': 58, 'category': 'Computer Mind', 'question': 'Some functionalists claim the brain is:', 'options': ['A soul', 'Like a computer', 'Not physical', 'An illusion'], 'correct': 1},
    {'id': 59, 'category': 'Computer Mind', 'question': 'The Turing Test attempts to determine:', 'options': ['If computers can calculate', 'If machines can think/have minds', 'If humans are smart', 'If bodies exist'], 'correct': 1},
    {'id': 60, 'category': 'Computer Mind', 'question': 'According to the computer view, minds:', 'options': ['Are immaterial souls', 'Process information like computers', 'Don\'t exist', 'Are mysterious'], 'correct': 1},
    {'id': 61, 'category': 'Computer Mind', 'question': 'John Searle\'s Chinese Room argument challenges:', 'options': ['Dualism', 'The claim that computers can understand', 'Behaviorism only', 'Identity theory only'], 'correct': 1},
    {'id': 62, 'category': 'Computer Mind', 'question': 'In Searle\'s Chinese Room, the person:', 'options': ['Understands Chinese', 'Follows rules without understanding', 'Is a computer', 'Has no consciousness'], 'correct': 1},
    {'id': 63, 'category': 'Computer Mind', 'question': 'Searle argues that syntax (symbol manipulation):', 'options': ['Is sufficient for semantics (meaning)', 'Is not sufficient for semantics', 'Proves computers think', 'Is irrelevant'], 'correct': 1},
    {'id': 64, 'category': 'Computer Mind', 'question': 'A computer passing the Turing Test would:', 'options': ['Prove it has consciousness', 'Show it can behave like it understands', 'Prove it has a soul', 'Be impossible'], 'correct': 1},
    {'id': 65, 'category': 'Computer Mind', 'question': 'The Chinese Room shows:', 'options': ['Computers definitely think', 'Symbol manipulation alone doesn\'t guarantee understanding', 'Dualism is true', 'Minds don\'t exist'], 'correct': 1},

    # Eliminative Materialism (8 questions)
    {'id': 66, 'category': 'Eliminative Materialism', 'question': 'What is eliminative materialism?', 'options': ['Mind and body both exist', 'Our ordinary mental concepts are false and should be eliminated', 'Eliminate the body', 'Eliminate science'], 'correct': 1},
    {'id': 67, 'category': 'Eliminative Materialism', 'question': 'Eliminative materialists like Paul Churchland claim:', 'options': ['Folk psychology is correct', 'Folk psychology is a false theory', 'Psychology is impossible', 'Only minds exist'], 'correct': 1},
    {'id': 68, 'category': 'Eliminative Materialism', 'question': '"Folk psychology" refers to:', 'options': ['Scientific psychology', 'Our everyday concepts of beliefs, desires, etc.', 'A type of music', 'Ancient wisdom'], 'correct': 1},
    {'id': 69, 'category': 'Eliminative Materialism', 'question': 'Eliminative materialists predict neuroscience will:', 'options': ['Prove dualism', 'Replace folk psychology with better concepts', 'Show minds don\'t exist at all', 'Prove religion'], 'correct': 1},
    {'id': 70, 'category': 'Eliminative Materialism', 'question': 'A major objection to eliminative materialism is:', 'options': ['It\'s too dualistic', 'To assert it, you must believe beliefs exist', 'It\'s too simple', 'It proves everything'], 'correct': 1},
    {'id': 71, 'category': 'Eliminative Materialism', 'question': 'Eliminative materialists argue our concepts of desire, belief, etc. are:', 'options': ['Perfect', 'Inadequate and will be replaced', 'Divine', 'Unnecessary to discuss'], 'correct': 1},
    {'id': 72, 'category': 'Eliminative Materialism', 'question': 'The theory suggests mental states might:', 'options': ['Be immaterial', 'Not exist as we currently conceive them', 'Be divine', 'Be perfectly understood'], 'correct': 1},
    {'id': 73, 'category': 'Eliminative Materialism', 'question': 'Critics say eliminative materialism:', 'options': ['Proves dualism', 'Is self-refuting (requires beliefs to deny beliefs)', 'Is obviously true', 'Proves nothing'], 'correct': 1},

    # Property Dualism / New Dualism (10 questions)
    {'id': 74, 'category': 'Property Dualism', 'question': 'What is property dualism?', 'options': ['Two substances exist', 'Physical things can have nonphysical properties', 'Property doesn\'t exist', 'Only minds exist'], 'correct': 1},
    {'id': 75, 'category': 'Property Dualism', 'question': 'David Chalmers argues:', 'options': ['Only physical properties exist', 'Consciousness is a nonphysical property', 'Minds don\'t exist', 'Behaviorism is true'], 'correct': 1},
    {'id': 76, 'category': 'Property Dualism', 'question': 'Property dualists claim:', 'options': ['There are two substances', 'There are two types of properties', 'Everything is illusion', 'Nothing exists'], 'correct': 1},
    {'id': 77, 'category': 'Property Dualism', 'question': 'Chalmers\' zombie argument involves beings that:', 'options': ['Are unconscious movie characters', 'Are physically identical to us but lack consciousness', 'Don\'t exist anywhere', 'Are supernatural'], 'correct': 1},
    {'id': 78, 'category': 'Property Dualism', 'question': 'If zombies are conceivable, Chalmers argues:', 'options': ['Materialism must be true', 'Consciousness must be nonphysical', 'Nothing exists', 'Everything is physical'], 'correct': 1},
    {'id': 79, 'category': 'Property Dualism', 'question': 'A zombie world would have:', 'options': ['No physical properties', 'All our physical properties but no consciousness', 'Only consciousness', 'Nothing'], 'correct': 1},
    {'id': 80, 'category': 'Property Dualism', 'question': 'Property dualism differs from Cartesian dualism because:', 'options': ['It denies physical properties', 'It doesn\'t claim two separate substances', 'It denies consciousness', 'It\'s not dualism'], 'correct': 1},
    {'id': 81, 'category': 'Property Dualism', 'question': 'Chalmers\' argument depends on:', 'options': ['Scientific proof', 'The conceivability of philosophical zombies', 'Religious faith', 'Mathematical proof'], 'correct': 1},
    {'id': 82, 'category': 'Property Dualism', 'question': 'New dualists believe consciousness:', 'options': ['Is purely physical', 'Cannot be fully explained physically', 'Doesn\'t exist', 'Is an illusion'], 'correct': 1},
    {'id': 83, 'category': 'Property Dualism', 'question': 'Property dualism tries to acknowledge:', 'options': ['Only physical science', 'Both physical facts and conscious experience', 'Neither mind nor body', 'Only consciousness'], 'correct': 1},

    # Critical Thinking / Methodology (15 questions)
    {'id': 84, 'category': 'Methodology', 'question': 'According to the textbook, when evaluating premises, you should first ask:', 'options': ['If the conclusion is true', 'If the claim fits your experience', 'If it\'s popular', 'If it\'s old'], 'correct': 1},
    {'id': 85, 'category': 'Methodology', 'question': 'When relying on experience to evaluate claims, you must ask:', 'options': ['Nothing', 'If your memory and senses were reliable in that case', 'If others agree', 'If it feels right'], 'correct': 1},
    {'id': 86, 'category': 'Methodology', 'question': 'The principle of charity in philosophy means:', 'options': ['Being nice', 'Interpreting arguments in their strongest plausible form', 'Giving money', 'Accepting everything'], 'correct': 1},
    {'id': 87, 'category': 'Methodology', 'question': 'To reconstruct an argument means to:', 'options': ['Destroy it', 'Restate it clearly with premises and conclusion', 'Ignore it', 'Memorize it'], 'correct': 1},
    {'id': 88, 'category': 'Methodology', 'question': 'A valid argument is one where:', 'options': ['The premises are true', 'If premises are true, conclusion must be true', 'Everyone agrees', 'It sounds good'], 'correct': 1},
    {'id': 89, 'category': 'Methodology', 'question': 'Socrates\' method involved:', 'options': ['Lecturing', 'Questioning to examine beliefs', 'Memorizing texts', 'Avoiding philosophy'], 'correct': 1},
    {'id': 90, 'category': 'Methodology', 'question': 'In the Crito dialogue, Socrates argues we should:', 'options': ['Always escape punishment', 'Only listen to the wise, not the many', 'Follow the majority', 'Avoid thinking'], 'correct': 1},
    {'id': 91, 'category': 'Methodology', 'question': 'Socrates claims we should listen to those who:', 'options': ['Are numerous', 'Have knowledge of right and wrong', 'Are powerful', 'Are wealthy'], 'correct': 1},
    {'id': 92, 'category': 'Methodology', 'question': 'When someone confuses experience with assumptions, they:', 'options': ['Are being careful', 'May claim certainty beyond what they actually experienced', 'Are always right', 'Should be trusted'], 'correct': 1},
    {'id': 93, 'category': 'Methodology', 'question': 'Descartes\' method of doubt involved:', 'options': ['Accepting everything', 'Doubting anything that could possibly be doubted', 'Ignoring philosophy', 'Following tradition'], 'correct': 1},
    {'id': 94, 'category': 'Methodology', 'question': 'According to the text, good philosophical thinking requires:', 'options': ['Quick judgments', 'Investigation, thinking, and ingenuity', 'Following authority', 'Avoiding questions'], 'correct': 1},
    {'id': 95, 'category': 'Methodology', 'question': 'The textbook emphasizes you should:', 'options': ['Accept all philosophical claims', 'Evaluate claims for yourself', 'Avoid thinking deeply', 'Follow the majority'], 'correct': 1},
    {'id': 96, 'category': 'Methodology', 'question': 'When analyzing an argument, you should identify:', 'options': ['Only the conclusion', 'Both the logical form and whether premises are true', 'Nothing', 'Only emotions'], 'correct': 1},
    {'id': 97, 'category': 'Methodology', 'question': 'A sound argument must be:', 'options': ['Popular', 'Valid with true premises', 'Complex', 'Ancient'], 'correct': 1},
    {'id': 98, 'category': 'Methodology', 'question': 'Philosophical questions often:', 'options': ['Have obvious answers', 'Require careful investigation and cannot be answered quickly', 'Should be avoided', 'Are meaningless'], 'correct': 1},

    # General Philosophy (12 questions)
    {'id': 99, 'category': 'General Philosophy', 'question': 'Philosophy literally means:', 'options': ['Love of wisdom', 'Love of science', 'Fear of ignorance', 'Love of books'], 'correct': 0},
    {'id': 100, 'category': 'General Philosophy', 'question': 'The question "What am I?" is primarily about:', 'options': ['Biology', 'Human nature and identity', 'Medicine', 'History'], 'correct': 1},
    {'id': 101, 'category': 'General Philosophy', 'question': 'Metaphysics is the study of:', 'options': ['Psychology', 'The fundamental nature of reality', 'Government', 'Art'], 'correct': 1},
    {'id': 102, 'category': 'General Philosophy', 'question': 'Epistemology is the study of:', 'options': ['Ethics', 'Knowledge and how we know things', 'Politics', 'Aesthetics'], 'correct': 1},
    {'id': 103, 'category': 'General Philosophy', 'question': 'The philosophical study of right and wrong is called:', 'options': ['Metaphysics', 'Ethics', 'Logic', 'Aesthetics'], 'correct': 1},
    {'id': 104, 'category': 'General Philosophy', 'question': 'A philosophical view that only matter exists is called:', 'options': ['Dualism', 'Materialism', 'Idealism', 'Pluralism'], 'correct': 1},
    {'id': 105, 'category': 'General Philosophy', 'question': 'Ancient Greek philosophy emphasized:', 'options': ['Avoiding questions', 'Rational inquiry and examination', 'Religious dogma', 'Political power'], 'correct': 1},
    {'id': 106, 'category': 'General Philosophy', 'question': 'The Socratic method involves:', 'options': ['Lecturing students', 'Asking questions to examine beliefs', 'Memorizing facts', 'Avoiding debate'], 'correct': 1},
    {'id': 107, 'category': 'General Philosophy', 'question': 'Continental philosophy (like existentialism) often focuses on:', 'options': ['Pure logic only', 'Human existence, meaning, and experience', 'Mathematics only', 'Science only'], 'correct': 1},
    {'id': 108, 'category': 'General Philosophy', 'question': 'Analytic philosophy typically emphasizes:', 'options': ['Mysticism', 'Logical analysis and clarity', 'Poetry', 'Religion'], 'correct': 1},
    {'id': 109, 'category': 'General Philosophy', 'question': 'Philosophy differs from science because it:', 'options': ['Rejects all evidence', 'Examines fundamental assumptions and concepts', 'Only uses experiments', 'Avoids reasoning'], 'correct': 1},
    {'id': 110, 'category': 'General Philosophy', 'question': 'The value of studying philosophy includes:', 'options': ['Getting easy answers', 'Developing critical thinking and examining assumptions', 'Avoiding hard questions', 'Memorizing facts'], 'correct': 1}
]

categories = ['all', 'Existentialism', 'Mind-Body', 'Behaviorism', 'Functionalism', 
              'Identity Theory', 'Computer Mind', 'Eliminative Materialism', 
              'Property Dualism', 'Methodology', 'General Philosophy']

resources = [
    {'title': 'Existentialism', 'url': 'https://plato.stanford.edu/entries/existentialism/', 'description': 'Comprehensive overview of existentialist philosophy including Sartre, Kierkegaard, and Camus'},
    {'title': 'Jean-Paul Sartre', 'url': 'https://plato.stanford.edu/entries/sartre/', 'description': 'Detailed examination of Sartre\'s philosophy, existentialism, and political thought'},
    {'title': 'Dualism', 'url': 'https://plato.stanford.edu/entries/dualism/', 'description': 'Overview of mind-body dualism and the arguments for and against substance dualism'},
    {'title': 'René Descartes', 'url': 'https://plato.stanford.edu/entries/descartes/', 'description': 'Complete entry on Descartes\' philosophy, method, and epistemology'},
    {'title': 'Plato', 'url': 'https://plato.stanford.edu/entries/plato/', 'description': 'Comprehensive resource on Plato\'s philosophy, dialogues, and theory of Forms'},
    {'title': 'Consciousness', 'url': 'https://plato.stanford.edu/entries/consciousness/', 'description': 'In-depth analysis of consciousness, qualia, and the hard problem'},
    {'title': 'Functionalism', 'url': 'https://plato.stanford.edu/entries/functionalism/', 'description': 'Explanation of functionalist theories of mind and mental states'},
    {'title': 'Behaviorism', 'url': 'https://plato.stanford.edu/entries/behaviorism/', 'description': 'Overview of philosophical and psychological behaviorism'},
    {'title': 'The Mind/Brain Identity Theory', 'url': 'https://plato.stanford.edu/entries/mind-identity/', 'description': 'Detailed examination of identity theory and reductionism'},
    {'title': 'The Chinese Room Argument', 'url': 'https://plato.stanford.edu/entries/chinese-room/', 'description': 'John Searle\'s famous argument against strong AI'},
    {'title': 'Eliminative Materialism', 'url': 'https://plato.stanford.edu/entries/materialism-eliminative/', 'description': 'Discussion of eliminativism and folk psychology'},
    {'title': 'Zombies', 'url': 'https://plato.stanford.edu/entries/zombies/', 'description': 'Philosophical zombies and Chalmers\' conceivability arguments'},
    {'title': 'Qualia', 'url': 'https://plato.stanford.edu/entries/qualia/', 'description': 'Analysis of qualitative conscious experience and its philosophical problems'},
    {'title': 'The Turing Test', 'url': 'https://plato.stanford.edu/entries/turing-test/', 'description': 'Overview of the Turing Test and machine intelligence'},
    {'title': 'Philosophy of Mind', 'url': 'https://plato.stanford.edu/entries/philosophy-mind/', 'description': 'General introduction to philosophy of mind and its major questions'},
    {'title': 'Rationalism vs. Empiricism', 'url': 'https://plato.stanford.edu/entries/rationalism-empiricism/', 'description': 'Historical and contemporary debates about sources of knowledge'},
    {'title': 'Socrates', 'url': 'https://plato.stanford.edu/entries/socrates/', 'description': 'Life, method, and philosophy of Socrates'},
    {'title': 'Critical Thinking', 'url': 'https://plato.stanford.edu/entries/logic-informal/', 'description': 'Informal logic, argumentation, and critical reasoning'},
    {'title': 'Feminist Philosophy of Mind', 'url': 'https://plato.stanford.edu/entries/feminism-mind/', 'description': 'Feminist critiques of traditional philosophy of mind'},
    {'title': 'Personal Identity', 'url': 'https://plato.stanford.edu/entries/identity-personal/', 'description': 'Philosophical questions about what makes you "you" over time'}
]

def get_filtered_questions():
    if st.session_state.selected_category == 'all':
        return questions
    return [q for q in questions if q['category'] == st.session_state.selected_category]

def calculate_score():
    filtered = get_filtered_questions()
    correct = sum(1 for q in filtered if st.session_state.answers.get(q['id']) == q['correct'])
    return correct, len(filtered)

def get_score_message(score, total):
    percentage = (score / total) * 100
    if percentage >= 90:
        return "Outstanding! Excellent mastery of PHL201 material."
    elif percentage >= 80:
        return "Very Good! Strong understanding of philosophical concepts."
    elif percentage >= 70:
        return "Good! Solid grasp of the material."
    elif percentage >= 60:
        return "Fair. Review the material for better understanding."
    else:
        return "Needs Improvement. Please review the course material carefully."

def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.show_results = False
    st.session_state.show_resources = False

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    .question-card {
        background: #F9FAFB;
        padding: 2rem;
        border-radius: 10px;
        border: 2px solid #E5E7EB;
        margin-bottom: 1rem;
    }
    .resource-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #E5E7EB;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .score-display {
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
        color: white;
        padding: 3rem;
        border-radius: 50%;
        text-align: center;
        display: inline-block;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .correct-answer {
        background: #D1FAE5;
        border: 2px solid #10B981;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .incorrect-answer {
        background: #FEE2E2;
        border: 2px solid #EF4444;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Resources Page
if st.session_state.show_resources:
    st.markdown('<div class="main-header"><h1>📚 Philosophy Resources</h1><p>Stanford Encyclopedia of Philosophy & Additional Resources</p></div>', unsafe_allow_html=True)
    
    if st.button("← Back to Assessment", type="primary"):
        st.session_state.show_resources = False
        st.rerun()
    
    st.info("""
    **About Stanford Encyclopedia of Philosophy**
    
    The Stanford Encyclopedia of Philosophy (SEP) is a dynamic reference work maintained by Stanford University. 
    It provides peer-reviewed, comprehensive entries on philosophical topics written by leading experts in the field. 
    All articles are freely accessible and regularly updated to reflect current scholarship.
    
    🔗 [Visit Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
    """)
    
    st.markdown("### 📖 Recommended Articles by Topic")
    
    col1, col2 = st.columns(2)
    
    for idx, resource in enumerate(resources):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(f"""
            <div class="resource-card">
                <h4 style="color: #4F46E5;">{resource['title']}</h4>
                <p style="font-size: 0.9rem; color: #6B7280;">{resource['description']}</p>
                <a href="{resource['url']}" target="_blank" style="color: #4F46E5; font-weight: 600;">Read Article →</a>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🌐 Additional Resources")
    st.markdown("""
    - **Internet Encyclopedia of Philosophy:** [https://iep.utm.edu/](https://iep.utm.edu/) - Peer-reviewed philosophical encyclopedia with accessible articles
    - **PhilPapers:** [https://philpapers.org/](https://philpapers.org/) - Comprehensive database of philosophy research and articles
    - **Philosophy Talk:** [https://www.philosophytalk.org/](https://www.philosophytalk.org/) - Radio show and podcast exploring philosophical ideas
    - **MIT OpenCourseWare - Philosophy:** [Free philosophy courses](https://ocw.mit.edu/courses/linguistics-and-philosophy/) - Free lecture notes and materials from MIT philosophy courses
    """)
    
    if st.button("Return to Assessment", type="primary", use_container_width=True):
        st.session_state.show_resources = False
        st.rerun()

# Results Page
elif st.session_state.show_results:
    score, total = calculate_score()
    percentage = (score / total) * 100
    
    st.markdown('<div class="main-header"><h1>🏆 PHL201 Assessment Results</h1><p>CognitiveCloud.ai - Xavier Honablue M.Ed</p></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div style="text-align: center; margin: 2rem 0;">
            <div class="score-display">
                <div>{percentage:.1f}%</div>
                <div style="font-size: 1.2rem; margin-top: 0.5rem;">{score} / {total}</div>
            </div>
            <h3 style="margin-top: 2rem;">{get_score_message(score, total)}</h3>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 📝 Question Review")
    
    filtered = get_filtered_questions()
    for idx, q in enumerate(filtered):
        user_answer = st.session_state.answers.get(q['id'])
        is_correct = user_answer == q['correct']
        
        if is_correct:
            st.markdown(f"""
            <div class="correct-answer">
                <strong>✅ Question {idx + 1}: {q['question']}</strong><br>
                <small><strong>Your answer:</strong> {q['options'][user_answer] if user_answer is not None else "Not answered"}</small><br>
                <small style="color: #4F46E5;"><strong>Category:</strong> {q['category']}</small>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="incorrect-answer">
                <strong>❌ Question {idx + 1}: {q['question']}</strong><br>
                <small><strong>Your answer:</strong> {q['options'][user_answer] if user_answer is not None else "Not answered"}</small><br>
                <small style="color: #10B981;"><strong>Correct answer:</strong> {q['options'][q['correct']]}</small><br>
                <small style="color: #4F46E5;"><strong>Category:</strong> {q['category']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Retake Assessment", type="primary", use_container_width=True):
            reset_quiz()
            st.rerun()
    with col2:
        if st.button("📚 View Philosophy Resources", use_container_width=True):
            st.session_state.show_resources = True
            st.rerun()

# Main Quiz Page
else:
    st.markdown('<div class="main-header"><h1>🧠 PHL201: Introduction to Philosophy</h1><p>CognitiveCloud.ai - Xavier Honablue M.Ed</p></div>', unsafe_allow_html=True)
    
    # Category Filter
    st.markdown("### 🎯 Filter by Category")
    selected = st.selectbox(
        "Choose a category:",
        options=categories,
        format_func=lambda x: 'All Categories' if x == 'all' else x,
        key='category_select'
    )
    
    if selected != st.session_state.selected_category:
        st.session_state.selected_category = selected
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.rerun()
    
    filtered = get_filtered_questions()
    
    # Progress Bar
    progress = (st.session_state.current_question + 1) / len(filtered)
    st.progress(progress)
    st.markdown(f"**Question {st.session_state.current_question + 1} of {len(filtered)}** | Category: **{filtered[st.session_state.current_question]['category']}**")
    
    # Current Question
    current_q = filtered[st.session_state.current_question]
    
    st.markdown(f"""
    <div class="question-card">
        <h3>📖 {current_q['question']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Answer Options
    answer = st.radio(
        "Select your answer:",
        options=range(len(current_q['options'])),
        format_func=lambda x: current_q['options'][x],
        key=f"q_{current_q['id']}",
        index=st.session_state.answers.get(current_q['id'])
    )
    
    if answer is not None:
        st.session_state.answers[current_q['id']] = answer
    
    # Navigation Buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.session_state.current_question > 0:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.current_question -= 1
                st.rerun()
    
    with col3:
        if st.session_state.current_question < len(filtered) - 1:
            if st.button("Next ➡️", type="primary", use_container_width=True):
                st.session_state.current_question += 1
                st.rerun()
        else:
            if st.button("✅ Submit Assessment", type="primary", use_container_width=True):
                st.session_state.show_results = True
                st.rerun()
    
    # Progress Info
    st.info(f"**Progress:** {len(st.session_state.answers)} of {len(filtered)} questions answered")
    
    # About Section
    with st.expander("ℹ️ About This Assessment"):
        st.markdown("""
        This comprehensive PHL201 assessment covers key topics from Introduction to Philosophy including:
        - **Existentialism** (Sartre)
        - **Mind-Body Problem**
        - **Dualism** (Plato, Descartes)
        - **Behaviorism** (Ryle)
        - **Functionalism** (Armstrong, Putnam)
        - **Identity Theory** (Smart)
        - **Computer Models of Mind** (Turing, Searle)
        - **Eliminative Materialism** (Churchland)
        - **Property Dualism** (Chalmers)
        - **Critical Thinking Methodology**
        
        The 110 questions are designed to test understanding of philosophical arguments, theories, and concepts.
        """)
        
        if st.button("📚 Explore Philosophy Resources"):
            st.session_state.show_resources = True
            st.rerun()
