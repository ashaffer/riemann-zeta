import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk2 :
    P2RoundedFactorCheckpointData.panel15Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix8_eq :
    P2RoundedFactorCheckpointData.panel15Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk2.1

theorem panel15Prefix9_eq :
    P2RoundedFactorCheckpointData.panel15Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk2.2.1

theorem panel15Prefix10_eq :
    P2RoundedFactorCheckpointData.panel15Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk2.2.2.1

theorem panel15Prefix11_eq :
    P2RoundedFactorCheckpointData.panel15Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk2.2.2.2

end RHP2Bridge
