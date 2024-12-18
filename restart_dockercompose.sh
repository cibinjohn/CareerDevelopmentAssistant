#!/bin/bash

# Create seperate endpoints for premium and scratch model responses
# keeping premium and scratch models the same
# Front end integration


sudo docker-compose down

working_dir=/home/cibin/Desktop/lambton/TERM3/capstone/pipeline/RAG/release_v4/CareerDevelopmentAssistant
#rag_dir=/home/cibin/Desktop/lambton/TERM3/capstone/pipeline/RAG/CareerDevelopmentAssistant
##


cd $working_dir/frontend
sudo docker build -t careerdevelopmentchatbot_ui:release_v4 .

#cd $working_dir/flaskapp
#sudo docker build -t careerdevelopmentchatbot:release_v4 .

#cd $working_dir/usercred_api
#sudo docker build -t careerdevelopmentchatbot_usercredapi:release_v4 .
#
#cd $working_dir/augmentgen_worker
#sudo docker build -t careerdevelopmentchatbot_augmentationmodel_worker:release_v4 .

#cd $working_dir/addressing_api
#sudo docker build -t careerdevelopmentchatbot_addressing_api:release_v4 .

###################################################
#echo "building addressmodel_worker"
#cd ../addressmodel_worker
#pwd
#sudo docker build -t careerdevelopmentchatbot_addressingmodel_worker:release_v4 .
#echo "built addressmodel_worker"


#cd $working_dir/augmentation_api
#echo "building rag"
#pwd
#sudo docker build -t  careerdevelopmentchatbot_rag:release_v4 .
#echo "rag built"


####################################################

cd $working_dir
sudo docker-compose up