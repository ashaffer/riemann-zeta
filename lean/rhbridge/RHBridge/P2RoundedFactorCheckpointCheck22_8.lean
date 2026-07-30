import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk8 :
    P2RoundedFactorCheckpointData.panel22Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix32_eq :
    P2RoundedFactorCheckpointData.panel22Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk8.1

theorem panel22Prefix33_eq :
    P2RoundedFactorCheckpointData.panel22Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk8.2.1

theorem panel22Prefix34_eq :
    P2RoundedFactorCheckpointData.panel22Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk8.2.2.1

theorem panel22Prefix35_eq :
    P2RoundedFactorCheckpointData.panel22Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk8.2.2.2

end RHP2Bridge
