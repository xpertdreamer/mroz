function [xzv,fmin,k]=met_dix(ak,bk,e,l)
%Метод дихотомии
%входные данные
%начальный интервал неопределенности L0=[ak, bk]
%e>0 малое число
%l>0 точность 

%шаг 2
k=0;
FlagIter=true;
while FlagIter
    %шаг 3
    yk=(ak+bk-e)/2;
    zk=(ak+bk+e)/2;
    %шаг 4
    if f(yk)<=f(zk)
        bk=zk; %изменяется правая граница, левая прежняя
    else
        ak=yk; %изменяется  левая граница, правая прежняя
    end
    %шаг 5
    %проверка уловия окончания
    if abs(bk-ak)<=l
        xzv=(ak+bk)/2;
        FlagIter=false;%процесс поиска завершен
    else
        k=k+1; %переход к следующей итерации
    end
end
fmin=f(xzv);
end