import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk8 :
    P2RoundedFactorCheckpointData.panel24Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix32_eq :
    P2RoundedFactorCheckpointData.panel24Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk8.1

theorem panel24Prefix33_eq :
    P2RoundedFactorCheckpointData.panel24Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk8.2.1

theorem panel24Prefix34_eq :
    P2RoundedFactorCheckpointData.panel24Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk8.2.2.1

theorem panel24Prefix35_eq :
    P2RoundedFactorCheckpointData.panel24Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk8.2.2.2

end RHP2Bridge
