import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk2 :
    P2RoundedFactorCheckpointData.panel5Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix8_eq :
    P2RoundedFactorCheckpointData.panel5Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk2.1

theorem panel5Prefix9_eq :
    P2RoundedFactorCheckpointData.panel5Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk2.2.1

theorem panel5Prefix10_eq :
    P2RoundedFactorCheckpointData.panel5Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk2.2.2.1

theorem panel5Prefix11_eq :
    P2RoundedFactorCheckpointData.panel5Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk2.2.2.2

end RHP2Bridge
