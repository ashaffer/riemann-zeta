import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel2FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel2FlatComponentChunk32

end RHP2Bridge
