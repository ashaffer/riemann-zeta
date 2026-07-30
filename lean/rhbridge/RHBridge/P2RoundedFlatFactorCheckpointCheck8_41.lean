import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel8FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel8FlatComponentChunk41

end RHP2Bridge
