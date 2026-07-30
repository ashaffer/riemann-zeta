import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk2 :
    P2RoundedFactorCheckpointData.panel22Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix8_eq :
    P2RoundedFactorCheckpointData.panel22Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk2.1

theorem panel22Prefix9_eq :
    P2RoundedFactorCheckpointData.panel22Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk2.2.1

theorem panel22Prefix10_eq :
    P2RoundedFactorCheckpointData.panel22Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk2.2.2.1

theorem panel22Prefix11_eq :
    P2RoundedFactorCheckpointData.panel22Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk2.2.2.2

end RHP2Bridge
