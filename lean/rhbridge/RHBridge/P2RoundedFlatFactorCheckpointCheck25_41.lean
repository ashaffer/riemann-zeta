import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel25FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel25FlatComponentChunk41

end RHP2Bridge
