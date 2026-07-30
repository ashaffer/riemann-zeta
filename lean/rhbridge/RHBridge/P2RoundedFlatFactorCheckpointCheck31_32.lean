import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel31FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel31FlatComponentChunk32

end RHP2Bridge
