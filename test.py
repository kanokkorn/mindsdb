from mindsdb import Predictor
import sys
import pandas as pd
import json
import time
import lightwood


lightwood.config.config.CONFIG.HELPER_MIXERS = False
mdb = Predictor(name='test_predictor')
#'rental_price',
#mdb.learn(to_predict=['neighborhood','rental_price'],from_data="https://mindsdb-example-data.s3.eu-west-2.amazonaws.com/home_rentals.csv",use_gpu=False,stop_training_in_x_seconds=1000, backend='lightwood', unstable_parameters_dict={'use_selfaware_model':True})

p = mdb.predict(when={'number_of_rooms': 3, 'number_of_bathrooms': 2, 'sqft':2411, 'initial_price':3000}, run_confidence_variation_analysis=True, use_gpu=True)
e = p[0].explanation

p_arr = mdb.predict(when_data='https://mindsdb-example-data.s3.eu-west-2.amazonaws.com/home_rentals.csv', use_gpu=True)
print(p_arr[0].explanation)

for p in p_arr:
    e = p.explanation

p = mdb.predict(when={'number_of_rooms': 3, 'number_of_bathrooms': 2, 'neighborhood': 'south_side', 'sqft':2411}, run_confidence_variation_analysis=True, use_gpu=True)

for p in p_arr:
    exp_s = p.epitomize()
    exp = p.explanation
    print(exp_s)

    print(p.as_dict())
    print(p.as_list())
    print(p.raw_predictions())
