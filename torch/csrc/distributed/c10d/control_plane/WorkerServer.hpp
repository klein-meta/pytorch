#pragma once

#include <string>

namespace c10d {
namespace control_plane {

class WorkerServer {
 public:
  WorkerServer(const std::string& socketFile);
};

}
}
