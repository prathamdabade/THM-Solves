import System.IO  
  
main = do  
    handle <- openFile "/home/prof/.ssh/id_rsa" ReadMode  
    contents <- hGetContents handle  
    putStr contents  
    hClose handle