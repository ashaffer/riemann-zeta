import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel9FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel9FlatComponentChunk41

end RHP2Bridge
