# VideoSearch Academy
VideoSearch Academy is an app created by Naadir Bakari, Salma Benderson, Joshua Saji, and Noah Cil for the MoCoHacks Hackathon (3/19/21-3/21/21).

The app provides the user with educational videos for their desired subject or topic, which they enter into the search bar. The user can filter the length of the videos that the app returns, having the option to find shorter or longer ones depending on what they are looking for.

AI uses a siamese neural network to output encodings of two strings - one being the user input and the other being the title of the video. The program will then use a similarity scoring function (which in this case is the difference of the sums of the encodings), and if it meets a certain threshold (under 1), then the strings are similar. This is essentially a helper function to help filter all the potential videos to display the user videos sorted based on relevancy to their problem
