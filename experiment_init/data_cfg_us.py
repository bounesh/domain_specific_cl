import sys

def train_data(no_of_tr_imgs,comb_of_tr_imgs):
    #print('train set list')
    if(no_of_tr_imgs=='tr10' and comb_of_tr_imgs=='c1'):
        # labeled_id_list=["01","02","04","16-3","16-8","16-9","16-10","16-11","16-12","16-13"]
        labeled_id_list=["03","05","16-1","16-6","16-7"]
    else:
        print('Error! Select valid combination of training images')
        sys.exit()
    return labeled_id_list

def val_data(no_of_tr_imgs,comb_of_tr_imgs):
    #print('val set list')
    if(no_of_tr_imgs=='tr10' and (comb_of_tr_imgs=='c1')):
        val_list=["16-2","16-4","16-5"]
    return val_list

def test_data():
    #print('test set list')
    test_list=["16-2","16-4","16-5"]
    return test_list
