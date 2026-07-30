import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk4 :
    P2RoundedFactorCheckpointData.panel22Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix16_eq :
    P2RoundedFactorCheckpointData.panel22Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk4.1

theorem panel22Prefix17_eq :
    P2RoundedFactorCheckpointData.panel22Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk4.2.1

theorem panel22Prefix18_eq :
    P2RoundedFactorCheckpointData.panel22Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk4.2.2.1

theorem panel22Prefix19_eq :
    P2RoundedFactorCheckpointData.panel22Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk4.2.2.2

end RHP2Bridge
