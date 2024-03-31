# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "The rules are not entirely independent of each other. For instance, Rule 7 contradicts Rule 2, as they propose divergent outcomes for individuals who are single and do not own homes."
    answers["(b) explain"] = "The rule set is not exhaustive. Considering new row - Home owner =yes, Marital Status= Divorced, Annual Income =Low, Currently Employed =No This row cannot be produced from any of the rules"
    answers["(c) explain"] = "Ordering could be necessary for this rule set to prioritize more specific rules over general ones. For example, applying Rule 7 before Rule 2 ensures that single individuals who are not homeowners are accurately classified."
    answers["(d) explain"] = "A default class may be necessary for instances where none of the rules are applicable. This default class would be assigned when the specified conditions are not met, serving as a fallback classification."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "To ensure mutual exclusivity among the rules, there should be no overlap between the conditions. They appear mutually exclusive as they categorize separate groups such as birds, fishes, mammals, and reptiles, each based on unique combinations of attributes"
    answers["(b) example"] = "There is no rule that covers amphibians, so under the given rules, a salamander would not be classified. This indicates that the rules are not exhaustive, as they do not provide a classification for every vertebrate in the dataset."
    answers["(c) example"] = "Because each rule assigns a different group without any overlap, the sequence in which they're used won't alter the classification result. Consequently, there's no need to worry about the order of these rules."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "The back-propagation algorithm leverages the chain rule of calculus to compute gradients efficiently by recursively applying the gradient of the loss from the output layer backward through the network, utilizing the gradient from each subsequent layer to compute the gradient of the preceding layer."
    answers["(b) explain"] = "Each layer's output is calculated from the previous layer's activations through weighted sums and activation functions, creating a direct computational chain from the input layer to the output layer."
    answers["(c) explain"] = "The vanishing gradient problem occurs when gradients of the loss function diminish significantly as they pass through the layers of a deep neural network during training. This results in slow or halted learning in the initial layers of the network.Training errors diminish to zero while test errors remain substantial, it is characteristic of overfitting, not the vanishing gradient problem."
    answers["(d) explain"] = "The statement is largely inaccurate because achieving perfect classification doesn't ensure zero gradients for all weights in a neural network. Gradients are influenced by factors such as loss and activation functions, and even slight deviations or numerical precision issues can result in non-zero gradients. These non-zero gradients allow for continued learning and fine-tuning of the network."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = "+"
    answers["(d) Row 2"] = "-"
    answers["(d) Row 3"] = "-"
    answers["(d) Row 4"] = "-"

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.38

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 50

    # explain_string
    answers["(a) explain"] = "k=5 offers a balance between generalization and sensitivity to local data structure by considering multiple neighbors. It helps mitigate the effects of noise and outliers while remaining less susceptible to random fluctuations compared to K=1. Additionally, K=5 avoids oversmoothing the local class information, which can occur with larger values such as K=50."
    answers["(b) explain"] = "With significant overlap between classes, a larger K could be advantageous. It would mitigate reliance on immediate neighbors, which could be misleading due to the overlap. A larger K could yield a more stable decision boundary in such a blended region."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "There are 5 + classes in total, among them they are 3  values where A=1"
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0 
    answers["(b) P(R|+)"] = 0.2
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "Naive Bayes of P(A=1|+)* P(B=1|+)* P(C=1|+) is 0.192 whereas for P(A=1|-)* P(B=1|-)* P(C=1|-) it is 0.032"
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "yes"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "yes"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "no"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "P(A=1|+)*P(B=1|+) = 0.2 which is not equal to P(A=1|+)*P(B=1|+) = 0.24. So A and B conditionally independent given class +"
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    #answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    #answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
