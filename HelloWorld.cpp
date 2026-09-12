#include <iostream>
#include <string>

class talk{
    private:
        std::string sentence = "Hello World!\n";
    public:
        
    //Getter
    const std::string& GetSentence() const{
        return sentence;
    }

    //Setter
    void SetSentence(const std::string& SetSentence) //& is refer to sentence
    {
        sentence = SetSentence;
    }

};


int main(){
    talk t;
    std::cout << t.GetSentence();
}