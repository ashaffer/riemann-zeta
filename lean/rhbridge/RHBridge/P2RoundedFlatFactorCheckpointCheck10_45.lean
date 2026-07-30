import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel10FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel10FlatComponentChunk45

end RHP2Bridge
