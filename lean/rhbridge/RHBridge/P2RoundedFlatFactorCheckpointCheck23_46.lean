import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel23FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel23FlatComponentChunk46

end RHP2Bridge
