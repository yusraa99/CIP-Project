pragma solidity >=0.7.0 <0.9.0;


//first build the investment contract with properties

contract Investment
{

    //for generate primary key
    uint public count = 0;
    Invest []  tempArr;
    CompanyInvestment []  tempCompany;


    // for company Invests 
    uint public cpyId = 0; 

    //id of invester , id of user , type 
    struct Wallet
    {
        uint id;
        string name;
        uint256 money;
        string currencyType;
        uint userId;
    }
    // struct for invest
    struct Invest 
    {
        uint investId;
        uint clientId;
        uint investerId;
        string investType;
        //user invest value
        uint user_value;
        //project id
        uint project_id;
    }

    struct CompanyInvestment
    {
        uint cInvstId;

        string name;
     
        //from database
        uint companyId;
        
        string country;
        
        uint256 last;

        uint256 hight;
 
        uint256 low;

        uint256 changePercentage;

    }



    //for generate primary key for each investment(uint)
    mapping(uint => Invest) public allInvest;
    //wallet mapping : 
    mapping(uint => Wallet) public allWallet;


    //company investment mapping
    mapping (uint => CompanyInvestment) public allCompanyInvestes;

    Invest [] public investers; //array to store all investment

    Wallet [] public wallets;

    //for company invests 
    CompanyInvestment [] public companyInvests;


    //CRUD
    //C: CREATE /Add/insert
    //R: read / show /print
    //U: UPDATE
    //D: DELETE


    function get() public view returns(Invest[] memory)
    {
        return tempArr;
    }
    //function for print array - read
    function ReadInvesters() public view returns(Invest [] memory)
    {
        return investers;
    }


    function AddInvest(uint investerId , uint clientId , string memory investType , uint uservalue, uint projectid) public returns (uint)
    {
        //increate the count for each add
        count++;
        Invest memory invest = Invest(count , clientId , investerId , investType,uservalue,projectid);
        allInvest[count] = invest;
        investers.push(allInvest[count]);
        return count;
    }


    //function to show all user's investments

    function ShowAllUserInvestments(uint userId) public returns(Invest[] memory)
    {
        delete tempArr;

        for(uint i = 0; i <investers.length;i++ )
        {
            if(investers[i].clientId == userId)
            {
                tempArr.push(investers[i]);
            }
        }
        return tempArr;
    }

    //function to delete investment for user

    function DeleteInvestment(uint userId , uint investId) public  returns (uint)
    {
        for(uint i = 0; i <investers.length;i++)
        {
            if(investers[i].clientId == userId && investers[i].investId == investId)
            {
                delete investers[i];
                return 1;
            }
        }
        return 0;
    }

     //function to update user invest 
    function UpdateUserInvest(uint userId , uint investerId,uint investid, uint uservalue, uint projectid , string memory investtype , uint user_value) public returns(uint)
    {

        Invest memory oldInvest = allInvest[investid]; // old values of invest
        //old values with new invest 
        Invest memory updatedInvest = Invest(oldInvest.investId , oldInvest.clientId ,oldInvest.investerId,investtype , user_value,oldInvest.project_id);
        allInvest[investid] = updatedInvest;
        for (uint i =0 ; i< investers.length;i++)
        {
            if(investers[i].clientId == userId && investers[i].investerId == investerId )
            {
                investers[i] = updatedInvest;
                break;
            }
        }
        return 1;
    }

    function AddWallet(uint id , string memory name , uint256 money ,string memory currencyType, uint userId) public returns(uint)
    {
            Wallet memory wa = Wallet(id,name,money,currencyType,userId); 
            allWallet[id] = wa; //add to mapping
            wallets.push(wa); // add to array
            return 1;
    }

    // show user wallet
    function ShowUserWallet(uint userId) public returns (Wallet memory)
    {
        for(uint i=0; i < wallets.length;i++)
        {
            if(wallets[i].userId == userId)
            {
                return wallets[i];
            }
        }

    }

    //function to update money inside wallet
    function UpdateUserWallet(uint userId , string memory name ,uint256 newMoney,string memory currencyType) public returns(uint)
    {
        Wallet memory oldWallet = allWallet[userId]; // old values of wallet
        //old values with new money 
        Wallet memory updatedWallet = Wallet(oldWallet.id , name , newMoney ,currencyType , userId);
        allWallet[userId] = updatedWallet;
        for (uint i =0 ; i< wallets.length;i++)
        {
            if(wallets[i].userId == userId)
            {
                wallets[i] = updatedWallet;
                break;
            }
        }
        return 1;
    }



    //company Investments

    function AddCompanyInvest(string memory name , uint companyId , string memory country,uint256 last,uint256 hight , uint256 low,uint256 changePercentage) public returns (uint)
    {
        //increate the count for each add
        cpyId++;

        CompanyInvestment memory invest = CompanyInvestment(cpyId, name , companyId , country,last,hight,low,changePercentage);
        
        allCompanyInvestes[cpyId] = invest;

        companyInvests.push(invest);

        return cpyId;
    }



    function DeleteCompanyInvestment(uint companyId , uint investId) public  returns (uint)
    {
        for(uint i = 0; i <companyInvests.length;i++)
        {
            if(companyInvests[i].companyId == companyId && companyInvests[i].cInvstId == investId)
            {
                delete companyInvests[i];
                return 1;
            }
        }
        return 0;
    }



    function UpdateCompanyInvest(uint companyId , uint investId,uint256 low,uint256 hight,uint256 last) public returns(uint)
        {
            CompanyInvestment memory oldcpy = allCompanyInvestes[investId]; // old values of wallet
            //old values with new money 
            CompanyInvestment memory updatedInvestment = 
            CompanyInvestment(oldcpy.cInvstId , oldcpy.name ,oldcpy.companyId,oldcpy.country,last,hight,low ,oldcpy.changePercentage);
            allCompanyInvestes[investId] = updatedInvestment;
            for (uint i =0 ; i< companyInvests.length;i++)
            {
                if(companyInvests[i].cInvstId == investId)
                {
                    companyInvests[i] = updatedInvestment;
                    break;
                }
            }
            return 1;
        }


function ShowAllCompanyInvestments(uint companyId) public returns(CompanyInvestment[] memory)
    {
        delete tempCompany;

        for(uint i = 0; i <companyInvests.length;i++ )
        {
            if(companyInvests[i].companyId == companyId)
            {
                tempCompany.push(companyInvests[i]);
            }
        }
        return tempCompany;
    }


}