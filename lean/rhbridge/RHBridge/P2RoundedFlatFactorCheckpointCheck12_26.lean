import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel12FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel12FlatComponentChunk26

end RHP2Bridge
