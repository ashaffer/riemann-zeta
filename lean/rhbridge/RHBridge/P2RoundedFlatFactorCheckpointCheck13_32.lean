import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel13FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel13FlatComponentChunk32

end RHP2Bridge
