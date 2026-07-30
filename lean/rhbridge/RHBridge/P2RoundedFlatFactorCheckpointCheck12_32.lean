import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel12FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel12FlatComponentChunk32

end RHP2Bridge
