import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel11FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel11FlatComponentChunk35

end RHP2Bridge
