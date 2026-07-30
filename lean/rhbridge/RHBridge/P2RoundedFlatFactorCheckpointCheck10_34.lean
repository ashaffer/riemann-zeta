import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel10FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel10FlatComponentChunk34

end RHP2Bridge
