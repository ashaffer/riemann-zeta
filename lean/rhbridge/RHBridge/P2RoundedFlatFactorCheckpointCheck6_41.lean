import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel6FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel6FlatComponentChunk41

end RHP2Bridge
