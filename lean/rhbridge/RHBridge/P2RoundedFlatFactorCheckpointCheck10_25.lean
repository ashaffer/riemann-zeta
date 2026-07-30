import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel10FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel10FlatComponentChunk25

end RHP2Bridge
