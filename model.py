import pickle
from happytransformer import HappyTextToText, TTTrainArgs

happy_tt = HappyTextToText("T5", "t5-base")

train_args = TTTrainArgs(
    batch_size=8,
    num_train_epochs=5,
    max_input_length=512,  
    max_output_length=150
)
happy_tt.train("Dataset/train.csv", args=train_args)

eval_args = TTTrainArgs(
    batch_size=8,
    max_input_length=512,
    max_output_length=150
)

happy_tt.eval("Dataset/eval.csv", args=eval_args)

pickle.dump(happy_tt, open('model.pkl','wb'))
