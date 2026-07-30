import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel21FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel21FlatComponentChunk32

end RHP2Bridge
