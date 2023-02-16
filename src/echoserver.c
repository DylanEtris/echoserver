#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv) {
  struct addrinfo hints, *res;
  hints.ai_family = AF_UNSPEC;
  hints.ai_socktype = SOCK_STREAM;
  hints.ai_flags = AI_PASSIVE;
  getaddrinfo(NULL, "10823", &hints, &res);
  int sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);

  if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &(int){1}, sizeof(int)) < 0) {
    printf("Failed during setsockopt\n");
    exit(1);
  }

  bind(sockfd, res->ai_addr, res->ai_addrlen);
  listen(sockfd, 5);
  for (;;) {
    int newsockfd = accept(sockfd, NULL, NULL);
    if (newsockfd < 0) {
      perror("ERROR on accept");
      exit(1);
    }
    char buf[1024];
    size_t numBytes = recv(newsockfd, buf, 1024, 0);
    send(newsockfd, buf, numBytes, 0);
    close(newsockfd);
  }
  close(sockfd);
  return 0;
}