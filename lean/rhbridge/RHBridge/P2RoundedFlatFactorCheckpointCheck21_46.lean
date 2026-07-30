import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel21FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel21FlatComponentChunk46

end RHP2Bridge
