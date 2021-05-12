import sys
def train_data():
    #print('train set list')
    labeled_id_list=["03","05","16-1","16-6","16-7"]
    return labeled_id_list
def pretrain_data():
    # labeled_id_list=["01","02","04","16-3","16-8","16-9","16-10","16-11","16-12","16-13"]
    labeled_id_list=["01"]
    return labeled_id_list
def val_data():
    # val_list=["16-2","16-4","16-5"]
    val_list=["16-2"]
    return val_list
def test_data():
    test_list=["16-2","16-4","16-5"]
    return test_list