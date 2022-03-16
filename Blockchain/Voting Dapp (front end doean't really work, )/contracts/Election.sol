// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.8.0;


contract Election {

    //---> V1 single candidate display
    //Read candidate, defining a var created a getter
    // string public candidate;

    // constructor() public {
    //     candidate = "Mr Minister bad";
    // }


    //----> V2 List of candidate, candidate extra data

    // A MODEL POJo for candidate
    struct Candidate{
        uint id;
        string name;
        uint voteCount;
    }

    // Store the  od candidate data
    // Fetch for model  HashMap<int, Cabdidate>
    mapping(uint => Candidate) public candidates;

    //Recoerd te voters
    mapping(address => bool) public voters;

    // Store the count of camdodate
    uint public candidatesCount;

    // voted event
    event votedEvent (
        uint indexed _candidateId
    );

    //constructon
    constructor() public {
        addCandidate("Mr bad minister");
        addCandidate("Mr very bad minister");
    }

    function addCandidate(string memory _name ) private {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
    }

    function vote(uint _candidateId) public {
        //Check acc has alreday voted
        require(!voters[msg.sender]);
        require(_candidateId > 0 && _candidateId < candidatesCount);

        //record voting ID, recoed who and all has voted
        msg.sender; //get the acc ID of votes
        voters[msg.sender] = true;

        // Update candidate vote count
        candidates[_candidateId].voteCount++;

        // trigger voted event
        emit votedEvent(_candidateId);
    }

}