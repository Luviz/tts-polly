# Text to Speech using AWS Polly 
This project is met to be an assistant to people (like me) with reading disorders. 

## My goals
The program need to be fast and assessable, I'm planing to use the clipboard.

```mermaid
flowchart LR
    
    S[Start]
    E[End]
    RC[Read form clipboard]
    HASH[Hash Content]
    CHECK[Check if string audio exist]
    IF{If exists}
    CALL[Call polly api]
    SAVE[Save]
    PLAY[Play audio]

    S --- RC --- HASH 
    HASH --- CHECK --- IF
    IF --> |no| CALL --- SAVE --> PLAY
    IF --> |yes| PLAY
    PLAY --> E

```

```mermaid
sequenceDiagram
    actor User
    participant Clip_Board
    participant TTS_Polly
    participant AWS_Polly

    User ->> Clip_Board: Copies Text
    User ->> TTS_Polly: Starts program
    activate TTS_Polly 
    TTS_Polly ->> Clip_Board: Reads 
    TTS_Polly ->> AWS_Polly: Request
    AWS_Polly ->> TTS_Polly: Responds
    TTS_Polly ->> User: play Audio file
    deactivate TTS_Polly 

```
