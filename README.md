<br />
<div align="center" id="readme-top">
  
  <h1 align="center">Leaderboard Submission Guide</h1>
  <h3 align="center">Deep Reinforcement Learning Class 2024 Programming Homework 4 | National Tsing Hua University</h3>

Due: 2024/05/14 (Tue.) 23:59

  <p align="center" >



<img src="docs/demo.gif" height=350>

Leaderboard Link: [http://project.aseart.com/s/FOB2023/deep](http://project.aseart.com/s/FOB2023/deep)

</div>



## Important Remainders

- DO NOT CHANGE anything in eval.py or git action, otherwise you will result in 0 score in leaderboard section.

- Make sure to allow CPU mode in your test agent.

- Make sure you pass checker.py checking before submitting to leaderboard.

- Please conisder submit to leaderboard ASAP and make improvements later, since the leaderboard would record the time of submission histories of each ID, and this might take into account when calculating the overall ranking score.

- You dont need to create any pull request now, simply push to your own repo, for the details please follow the instructions shown in below.



## Leaderboard Submission

We provide a leaderboard for you to compare with your classmate, the ranking of which will be a significant reference of your overall score based on your relative ranking position.  

To submit your code to leaderboard, you will need to first **fork this repo**. Then in your forked repo, enter `Actions` tag, and click `I understand my workflows, go ahead and enable them`:

<img src="docs/action.png">


Then clone it to your local environment:

```
git clone <Your forked repo> 
```

Now replace `112062892_hw4_test.py` and `112062892_hw4_data` in the repo with your own version of them. The following packages were installed by default in repo cloud environment:

- Python 3.6.1
- tdqm
- requests
- osim-rl
- scipy
- torch (CPU)

If you wish to add more dependencies inorder to run your code, please add them into `requirements.txt`, each raw for one dependency.

Then change the name in `meta.xml` to your **STUDENT ID** for the submission. Note that if you submit to leaderboard multiple times when you improved the agent, simply use the same name and the result will be updated. Please make sure the id here consistents with the id shows on the name of your test file.

```
<?xml version="1.0"?>
<catalog>
   <info>
      <name>CHANGE HERE INTO YOUR ID</name> 
   </info>
</catalog>
```

Once you are happy with above, commit & push them to your forked repo:

```
git add .
git commit -m "submission"
git push
```

Pushing to the repo will trigger the following procedure:

1. Creating virtual env
2. installing dependencies
3. Run your code and return a score if checking succeed and Push the socre to the leaderboard


This might need some time since the leaderboard are running on CPU, you could check the progress of it by clicking the orange dot showing in below [Top left near "submission" in the pic.] then in the pop-up window clike "details", if the any of above workflow fails, you could view details in it.

<img src="docs/example.png">

