import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel25FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel25FlatComponentChunk46

end RHP2Bridge
