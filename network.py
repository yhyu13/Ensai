from model.ensai_model import *

y_mod = []
with tf.variable_scope("ENSAI"):

    y_mod.insert( 0 , model_1(x_image,scope="EN_Model1"  ))
    y_mod.insert( 1 , model_2(x_image,scope="EN_Model2"  ))
    y_mod.insert( 2 , model_3(x_image,scope="EN_Model3"  ))
    y_mod.insert( 3 , model_4(x_image,scope="EN_Model4"  ))
    y_mod.insert( 4 , model_5(x_image,scope="EN_Model5"  ))
    y_mod.insert( 5 , model_6(x_image,scope="EN_Model6"  ))
    y_mod.insert( 6 , model_7(x_image,scope="EN_Model7"  ))
    y_mod.insert( 7 , model_8(x_image,scope="EN_Model8"  ))
    y_mod.insert( 8 , model_9(x_image,scope="EN_Model9"  ))
    y_mod.insert( 9 , model_10(x_image,scope="EN_Model10"  ))

    execfile("nets/inception_utils.py")
    execfile("nets/inception.py")
    arg_scope = inception_v4_arg_scope()
    input_tensor =  tf.reshape(x, [-1,numpix_side,numpix_side,1])
    input_tensor = tf.concat([input_tensor,input_tensor,input_tensor], axis=3)
    with tf.variable_scope("EN_Model11"):
        with slim.arg_scope(arg_scope):
            y_mod.insert(10,  inception_v4( input_tensor , num_classes = 5 , dropout_keep_prob=1.0 , is_training=False,create_aux_logits=False) )


#chose model: 5:OverFeat, 8:our made-up model, 9:AlexNet, 11:Inception.v4. Defaults to AlexNet if nothing specified 
if 'model_num' not in locals():
    print("No model selected. Selecting default model (9: AlexNet).")
    model_num = 9
y_conv = y_mod[model_num-1] 



variables_to_save =  slim.get_variables(scope="ENSAI/EN_Model" + str(model_num) )   #list of variables to save
variables_to_restore = variables_to_save   #list of variables to restore (same as save here)
train_pars = variables_to_save  #list of parameters to train



save_file =  "data/trained_weights/model_" + str(model_num) + ".ckpt"     #path of file to save
restore_file = save_file   #path of network weights file to restore from

RESTORE = True
SAVE = False
restorer = tf.train.Saver(variables_to_restore)
saver = tf.train.Saver(variables_to_save)



############## flipping and cost function
MeanSquareCost , y_conv_flipped = cost_tensor(y_conv)
